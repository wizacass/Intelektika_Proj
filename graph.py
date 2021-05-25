import matplotlib.pyplot as plt
import numpy as np
import math
from collections import Counter


class Grapher:
    def __init__(self, dataset: str):
        self.dataset = dataset

    def histo(self, attribute, binary=False):

        if binary:
            counter = Counter(attribute.values)
            plt.bar(counter.keys(), counter.values())
        else:
            counts, bins = np.histogram(attribute.values)
            plt.hist(bins[:-1], bins, weights=counts)

        plt.xlabel(attribute.name)
        plt.ylabel("Count")
        plt.savefig(f"results/graphs/{self.dataset}/{attribute.name}.png")
        plt.clf()

    def scatter(self, attributeX, attributeY):

        plt.xlabel(attributeX.name)
        plt.ylabel(attributeY.name)
        plt.scatter(attributeX.values, attributeY.values, alpha=0.5)
        plt.savefig(
            f"results/graphs/{self.dataset}/{attributeX.name} on {attributeY.name}.png")
        plt.clf()

    def splom(self, attributes):
        count = len(attributes)
        r = range(0, count)
        for i in r:
            for j in r:
                ax = plt.subplot2grid((count, count), (i, j))
                ax.set_axis_off()
                if i != j:
                    ax.scatter(
                        attributes[i].values,
                        attributes[j].values,
                        s=0.5, alpha=0.25
                    )

        plt.savefig(
            f"results/graphs/{self.dataset}/splom.png",
            dpi=1200
        )
        plt.clf()

    def bar_plot(self, attribute, label=""):
        counter = Counter(attribute.values)
        plt.bar(counter.keys(), counter.values())
        plt.xlabel(attribute.name)
        plt.ylabel("Count")
        plt.savefig(
            f"results/graphs/{self.dataset}/bar_{attribute.name} {label}.png")
        plt.clf()

    def box_plot(self, attributes: list, labelX: str, labelY: str):
        plt.boxplot(attributes)
        plt.xticks([1, 2], ["True", "False"])
        plt.xlabel(labelX)
        plt.ylabel(labelY)
        plt.savefig(
            f"results/graphs/{self.dataset}/box_{labelX} on {labelY}.png")
        plt.clf()

    def correlation_matrix(self, correlation_data: list, labels: list):
        plt.matshow(correlation_data)
        plt.colorbar()
        plt.xticks(range(0, len(correlation_data[0])), labels, rotation=45)
        plt.yticks(range(0, len(correlation_data[1])), labels, rotation=45)
        plt.savefig(
            f"results/graphs/{self.dataset}/correlation_matrix.png")
        plt.clf()

    def __column_count(self, size):
        count = 1 + 3.22 * (math.log(math.e) ** size)

        return int(round(count))
