#
# Semantic Rules
#

class WrongDimensionException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class WrongExpressionException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class WrongPointFormatException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class WrongPointDimensionException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class NoBinaryClassificationTagNameSpaceException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class EpochsNotANumberException(Exception):
    def __init__(self, msg):
        super().__init__(msg)