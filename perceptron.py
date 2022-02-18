import argparse
import logging
import numpy as np

import data_parser

logging.basicConfig(filename="runtime.log", level=logging.INFO)

parser = argparse.ArgumentParser(description="Simple Perceptron Implementation")
parser.add_argument("file", help="Defines the file where the data is stored in to train the perceptron")
args = parser.parse_args()
print(args.file)

logging.info("Running perceptron")

points, tags = data_parser.read_file(args.file)

points = map( lambda n: n.append(float(1.0)) , points )

points2 = list(points)
points = np.array(points, np.float32)



shape = points2.shape
dtype = points2.dtype



print("Nothing")