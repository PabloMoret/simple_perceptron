import re
import logging
import exceptions
import ast
import os

logging.basicConfig(filename="runtime.log", level=logging.INFO)

def read_file(file):

    if not os.path.isfile(file):
        logging.error("Error while opening file. Check file path")
        raise FileNotFoundError("File {file} not found".format(file=file))

    logging.info("Reading data from {file}".format(file=file))
    f = open(file, "r")
    dimension = f.readline().strip()
    if(not re.search(r'[2-9]', dimension)):
        logging.error("Wrong Dimension Format! Range from 2 to 9. Check example file for details")
        raise exceptions.WrongDimensionException("Check format and space dimension in input file")
    dimension = int(dimension)
    
    points = []
    tags = []
    tags_namespace = []
    
    lines = f.readlines()
    if not lines:
        logging.error("Wrong Points Format! Make sure points have proper format. Check example file for details")
        raise exceptions.WrongPointFormatException("Check points format.")

    for i, l in enumerate(lines):
        l = l.strip()
        #if(not re.search(r'^\[(-\d,|\d,)+(-\d|\d)\],[a-zA-Z]$', l)):
        if(not re.search(r'^\[(-\d+,|\d+,|-\d+\.\d+,|\d+\.\d+,|\.\d+,|-\.\d+,)+(-\d+|\d+|-\d+\.\d+|\d+\.\d+|\.\d+|-\.\d+)\],[a-zA-Z]+$', l)):
            logging.error("Wrong Points Expression! Correct format: array of integers comas separated followed by a coma and any letter [a-zA-Z]. Check example file for detail")
            raise exceptions.WrongExpressionException("Check points expressions in input file file. Line {lineNumber}".format(lineNumber=i+1))
        
        #point = ast.literal_eval(re.match(r'^\[(-\d,|\d,)+(-\d|\d)\]', l).group())
        point = ast.literal_eval(re.match(r'^\[(-\d+,|\d+,|-\d+\.\d+,|\d+\.\d+,|\.\d+,|-\.\d+,)+(-\d+|\d+|-\d+\.\d+|\d+\.\d+|\.\d+|-\.\d+)\]', l).group())
        point = list(map(lambda any_number: float(any_number), point))
        if(len(point) != dimension):
            logging.error("Wrong Point Dimension! Check the points dimension")
            raise exceptions.WrongPointDimensionException("Check points dimension. Space dimension {spaceDim} but found point of size {pointDim}".format(spaceDim=dimension, pointDim=i))
        points.append(point)

        tag = re.search(r'\,[a-zA-Z]+$', l).group().replace(',','')
        if tag not in tags_namespace: tags_namespace.append(tag)
        tags.append(tag)

    if (len(tags_namespace) != 2):
        logging.error("Point tags do not follow binary classification. Check tags names")
        raise exceptions.NoBinaryClassificationTagNameSpaceException("Make sure the tags namespace is binary")

    f.close()

    return points, tags