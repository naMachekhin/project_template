import pandas as pd

def console_input(prompt=""):
    '''
    Reads data from console using puthon built-in

    Parameters:
        prompt: prompt text, must be convertable to string
    Raises:
        ValueError: Object is not convertible to string
    Returns:
        str: data read from console
    '''
    try:
        pr=str(prompt)
        return input(pr)
    except TypeError:
        raise ValueError("Object is not convertible to string") from None




def open_file(path):
    '''
    Reads data from given file using pythob bult-in
    Parameters:
        path (str): path to the file
    Raises:
        FileNotFoundError: Cannot read file
    Returns:
        str: data from read file
    '''
    try:
        file = open(path, 'r')
        data=file.read()
        file.close()
        return data
    except:
        raise FileNotFoundError("Cannot read file") from None



def open_file_pandas(path):
    '''
    Reads data from given file using pandas
    Parameters:
        path (str): path to the file
    Raises:
        FileNotFoundError: Cannot read file
    Returns:
        str: data from read file
    '''
    try:
        data=pd.read_csv(path, header=None)
        return str(data)
    except:
        raise FileNotFoundError("Cannot read file") from None
