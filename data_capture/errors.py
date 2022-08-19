"""Custom errors and warnings"""


class DataCaptureError(Exception):
    pass


class OutOfRangeError(DataCaptureError):
    pass


class InvalidTypeError(DataCaptureError):
    pass


class LackOfDataWarning(ResourceWarning):
    pass
