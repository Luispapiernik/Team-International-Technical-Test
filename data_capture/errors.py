class DataCaptureError(Exception):
    pass


class OutOfRangeError(DataCaptureError):
    pass


class LackOfDataWarning(ResourceWarning):
    pass
