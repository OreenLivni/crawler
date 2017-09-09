import os


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
        file_to_write.write(data + '\n')


def delete_file_if_exists(file_name):
    """
    checks if the received file exists, if it does it deletes it's content.
    :param file_name: the file name to change.
    :type file_name: str
    """
    try:
        os.remove(file_name)
    except OSError:
        pass


def get_site_name(url):
    """
    the function returns the site name. for example if the received url is 'https//health.com' the function will return
    'health'.
    :param url: the site's url
    :type url: str
    :return: the site's name according to the url.
    :rtype: str
    """
    if url.startswith('https'):
        url = url.replace('https://', '')
        print url
    elif url.startswith('http'):
        url = url.replace('http://', '')

    # if url.endswith('.com'):
    #     url = url.replace('.com', '')
    return url

