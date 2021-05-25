class Song:
    def __init__(self, data_string: str):
        data = data_string.split(';')

        if len(data) != 12:
            raise ValueError('Invalid string provided!')

        # The relative metric of the track being acoustic
        self.acousticness = float(data[0])

        # The relative measurement of the track being danceable
        self.danceability = float(data[1])

        # The duration of the track in seconds
        self.duration = int(data[2]) / 1000

        # The energy of the track
        self.energy = float(data[3])

        # The binary value whether the track contains explicit content or no
        self.explicit = str(bool(int(data[4])))

        # The relative duration of the track sounding as a live performance
        self.liveness = float(data[5])

        # The overall loudness of a track in decibels (dB)
        self.loudness = float(data[6])

        # The binary value representing whether the track starts with a major (1) chord progression or not (0)
        self.mode = "Major" if data[7] == "1" else "Minor"

        # The popularity of the song lately, default country = US
        self.popularity = int(data[8])

        # The overall estimated tempo of a track in beats per minute (BPM)
        self.tempo = float(data[9])

        # A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track
        self.valence = float(data[10])

        # The release year of track
        self.year = int(data[11])


class SongsList:
    def __init__(self):
        self.acousticness = Attribute("acousticness")
        self.danceability = Attribute("danceability")
        self.duration_s = Attribute("duration_s")
        self.energy = Attribute("energy")
        self.explicit = Attribute("explicit")
        self.liveness = Attribute("liveness")
        self.loudness = Attribute("loudness")
        self.mode = Attribute("mode")
        self.popularity = Attribute("popularity")
        self.tempo = Attribute("tempo")
        self.valence = Attribute("valence")
        self.year = Attribute("year")
        self.size = 0

        self.numerical_attr = [
            self.acousticness,
            self.danceability,
            self.duration_s,
            self.energy,
            self.liveness,
            self.loudness,
            self.popularity,
            self.tempo,
            self.valence,
        ]

        self.categorical_attr = [
            self.explicit,
            self.mode,
            self.year
        ]

    def add_song(self, song: Song):
        self.acousticness.append(song.acousticness)
        self.danceability.append(song.danceability)
        self.duration_s.append(song.duration)
        self.energy.append(song.energy)
        self.explicit.append(song.explicit)
        self.liveness.append(song.liveness)
        self.loudness.append(song.loudness)
        self.mode.append(song.mode)
        self.popularity.append(song.popularity)
        self.tempo.append(song.tempo)
        self.valence.append(song.valence)
        self.year.append(song.year)
        self.size += 1

    def explicit_songs_popularity(self, explicit: bool):
        is_explicit = "True" if explicit else "False"
        data = Attribute("popularity")
        for i in range(0, self.size):
            if self.explicit.at(i) == is_explicit:
                data.append(self.popularity.at(i))

        return data

    def mode_popularity(self, mode: bool):
        is_major = "Major" if mode else "Minor"
        data = Attribute("popularity")
        for i in range(0, self.size):
            if self.mode.at(i) == is_major:
                data.append(self.popularity.at(i))

        return data

    def explicit_valence(self, explicit: bool):
        is_explicit = "True" if explicit else "False"
        data = Attribute("valence")
        for i in range(0, self.size):
            if self.explicit.at(i) == is_explicit:
                data.append(self.valence.at(i))

        return data

    def __str(self):
        return f"There are {self.size} songs data"

    def __str__(self):
        return self.__str()

    def __repr__(self):
        return self.__str()


class Attribute:
    def __init__(self, name: str):
        self.name = name
        self.values = []

    def append(self, value):
        self.values.append(value)

    def at(self, i: int):
        return self.values[i]

    def __repr__(self):
        return f"{name} data"
