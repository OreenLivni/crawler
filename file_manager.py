
class FileManager:
    """ this class contains functions made to handle the files logic. """

    def __init__(self):
        """ the initializer """
        pass

def append_to_file(file_name, data):
    """
    this function receives a file_name and the data to write to it and writes to it the data.
    :param file_name: the file name to write to.
    :type file_name: str
    :param data: date to write to the file.
    :type data: str
    """

    with open(file_name, 'a') as file_to_write:
        file_to_write.write(data)

