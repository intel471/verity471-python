class VerityStixException(Exception):
    pass


class StixMapperNotFound(VerityStixException):
    pass


class EmptyBundle(VerityStixException):
    pass
