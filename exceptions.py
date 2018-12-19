class SizeTypeError(Exception):
    def __init__(self, size_type):
        raise Exception("\'" + size_type + "\'" + " don't support size-type you should input follow as \'B\', \'K\', \'M\', \'G\', \'T\' or Empty")
