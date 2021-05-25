from song import Song, SongsList
from graph import Grapher
from analyzer import Analyzer

dataset = "2010-2020"


def read(path: str):
    songs = SongsList()
    file = open(path, "r")
    file.readline()
    for line in file:
        try:
            song = Song(line)
            songs.add_song(song)
        except:
            print("Inavlid data row found!")
            continue

    file.close()

    return songs


def write(path: str, lines: list):
    file = open(path, "w")
    for line in lines:
        file.write(line)

    file.close()


def draw_scatters(songs: SongsList, grapher: Grapher):
    grapher.scatter(
        songs.duration_s,
        songs.liveness,
    )

    grapher.scatter(
        songs.liveness,
        songs.acousticness,
    )


def create_header(attributes):
    header = ""
    for attr in attributes:
        header += f"{attr.name};"

    return header


def remove_outliers(attributes: list, a: Analyzer):
    for attr in attributes:
        attr.values = a.remove_outliers(attr.values)


def main():
    songs = read(f"data/{dataset}.csv")
    g = Grapher(dataset)
    a = Analyzer(songs.size)

    remove_outliers(songs.numerical_attr, a)
    draw_scatters(songs, g)

    print("Done!")


main()
