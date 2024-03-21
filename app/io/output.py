

def console_output(data):
    '''
    Prints string to console
    Parameters:
        data : data to print, must be convertible to string
    Raises:
        ValueError: Object is not convertible to string
    '''
    try:
        print(str(data))
    except TypeError:
        raise ValueError("Object is not convertible to string") from None

def file_write(path, data):
    '''
    Prints given data to given file
    Parameters:
        path (str): path to file
        data : data to print, must be convertible to string
    Raises:
        ValueError: Object is not convertible to string
        FileNotFoundError: Cannot write to file
    '''

    try:
        str_data=str(data)
    except TypeError:
        raise ValueError("Object is not convertible to string") from None
    try:
        file=open(path, "w")
        file.write(str_data)
        file.close()
    except:
        raise FileNotFoundError("Cannot write to file") from None