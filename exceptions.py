class SizeTypeError(Exception):
    def __init__(self, size_type):
        self.size_type = size_type
        self.message = " don't support size-type you should input follow as \'B\', \'K\', \'M\', \'G\', \'T\' or Empty"

    def __str__(self):
        return str("\'" + self.size_type + "\'" + self.message)


class InvalidUrl(Exception):
    def __init__(self, url):
        self.url = url
        self.message = " is not valid."

    def __str__(self):
        return str(self.url + self.message)


class NotGoogleDriveUrl(Exception):
    def __init__(self, url):
        self.url = url
        self.message = " is not Google Drive Url"

    def __str__(self):
        return str(self.url + self.message)


class NotFoundGoogleDriveUrl(Exception):
    def __init__(self, url):
        self.url = url
        self.message = " Not Found"

    def __str__(self):
        return str(self.url + self.message)
