import argparse
import logging
import numpy as np

import data_parser

logging.basicConfig(filename="runtime.log", level=logging.INFO)

def tagsToNumber(tags, tags_namespace):
    primary = tags[0]
    tags = list(map(lambda t: 0 if t == primary else 1, tags))
    tags_namespace = list(map(lambda t: 0 if t == primary else 1, tags_namespace))
    return tags, tags_namespace

def toNumpyArray(points, dimension):
    """Transforms input points to numpy array. Generates initial weights numpy array

    Args:
        points (2D array): array containing n dimensional points
        dimension (int): space dimension
    
    Returns:
        points: 2D numpy array of points
        weights: 1D numpy array of weights
    """
    points = list(map(lambda n: n + [float(1.0)] , points))
    points = np.array(points, np.float32)
    weights = np.array(points[0], copy=True)
    return points, weights

def perceptron(points, tags, tags_namespace, dimension, epochs, weights):
    """Runs Perceptron Algorithm

    Args:
        points (2D nd array): array containing n dimensional points
        tags (1D array): array containing binary tags of respective points
        dimension (int): space's dimension
        epochs (int): number of iterations to run the algorithm
        weights (1D nd array): array containing weights of perceptron
    
    Returns
    """
    counter = 0
    while counter <= epochs:
        classified = 0
        for point, tag in zip(points, tags):
            if (tag == 0 and np.dot(weights, point)<0):
                weights = np.add(weights, point)
                classified = 1
            if (tag == 1 and np.dot(weights, point)>=0):
                weights = np.subtract(weights, point)
                classified = 1
        if not classified:
            logging.info("Run {number} epochs to train perceptron".format(number=counter))
            break
    if (counter == epochs):
        logging.error("Algorithm could not train perceptron to correctly classified all the points")
    
    return weights

parser = argparse.ArgumentParser(description="Simple Perceptron Implementation")
parser.add_argument("file", help="Defines the file where the data is stored in to train the perceptron")
parser.add_argument("epochs", help="Defines the maximum number of epochs to be run to train perceptron")
args = parser.parse_args()
print(args.file)

logging.info("Running perceptron")

points, tags, tags_namespace, dimension, epochs = data_parser.read_file(args.file, args.epochs)

tags, tags_namespace = tagsToNumber(tags, tags_namespace)

points, weights = toNumpyArray(points, dimension)

weights = perceptron(points, tags, tags_namespace, dimension, epochs, weights)



print("Nothing")