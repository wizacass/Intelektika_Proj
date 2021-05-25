from collections import Counter
import statistics
from song import Attribute


class Analyzer:
    def __init__(self, size: int):
        self.size = size
        self.factor = 2

    def analyze_numerical(self, property):
        sorted_prop = sorted(property)
        amount = len(property)
        props = []

        # amount
        props.append(amount)

        # missing
        props.append(self.size - amount)

        # cardinality
        props.append(len(set(property)))

        # minimum
        props.append(sorted_prop[0])

        # maximum
        props.append(sorted_prop[amount - 1])

        # 25 percentile
        props.append(sorted_prop[self.__q_index(sorted_prop, 25)])

        # 75 percentile
        props.append(sorted_prop[self.__q_index(sorted_prop, 75)])

        # average
        props.append(self.__average(property))

        # median
        props.append(statistics.median(property))

        # standard deviation
        props.append(round(statistics.stdev(property), 3))

        return self.__to_csv_row(props)

    def analyze_categorical(self, property):
        counter = Counter(property)
        amount = len(property)

        props = []
        props.append(amount)  # amount
        props.append(self.size - amount)  # missing
        props.append(len(set(property)))  # cardinality

        props.extend(self.__analyze_mode(counter, 1, amount))  # mode
        props.extend(self.__analyze_mode(counter, 2, amount))  # mode

        return self.__to_csv_row(props)

    def __average(self, property):
        avg = sum(property) / len(property)

        return round(avg, 3)

    def __q_index(self, sorted_list, index):
        length = len(sorted_list)

        return int(round(length * (index) / 100))

    def __to_csv_row(self, props):
        line = ""
        for prop in props:
            line += f"{str(prop)};"

        return line

    def __analyze_mode(self, counter, mode_index, size):
        lines = []
        mode_stats = counter.most_common()
        frequency = mode_stats[mode_index - 1][1]

        lines.append(str(mode_stats[mode_index - 1][0]))  # mode
        lines.append(frequency)  # mode_freq
        lines.append(round(frequency / size * 100, 2))  # mode percentage

        return lines

    def remove_outliers(self, property):
        new_data = []
        sorted_prop = sorted(property)

        q1 = sorted_prop[self.__q_index(sorted_prop, 25)]
        q3 = sorted_prop[self.__q_index(sorted_prop, 75)]
        iqr = q3 - q1

        lower = q1 - self.factor * iqr
        higher = q3 + self.factor * iqr

        for x in property:
            if x < lower:
                new_data.append(lower)
            elif x > higher:
                new_data.append(higher)
            else:
                new_data.append(x)

        return new_data

    def normalize(self, attribute: Attribute):
        data = Attribute(attribute.name)
        min_value = min(attribute.values)
        max_value = max(attribute.values)
        div = min_value - max_value

        for val in attribute.values:
            normalized = (val - min_value) / div
            data.append(normalized)

        return data

    def covariation(self, attribute_x, attribute_y):
        cov = 1 / (self.size - 1)
        s = 0

        avg_x = self.__average(attribute_x)
        avg_y = self.__average(attribute_y)
        for i in range(0, self.size):
            c = (attribute_x[i] - avg_x) * (attribute_y[i] - avg_y)
            s += c

        return cov * s

    def correlation(self, attribute_x, attribute_y):
        div = statistics.stdev(attribute_x) * statistics.stdev(attribute_y)

        return self.covariation(attribute_x, attribute_y) / div
