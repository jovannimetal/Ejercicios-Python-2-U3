class StudentsDataException(Exception):
    pass


class WrongLine(StudentsDataException):
    def __init__(self, message):
        StudentsDataException.__init__(self)
        print(message)
        exit()


class FileEmpty(StudentsDataException):
    def __init__(self, message):
        StudentsDataException.__init__(self)
        print(message)
        exit()


