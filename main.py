from app.io.input import *
from app.io.output import *



def main():
    data= console_input("enter text:")+"\n----\n"+open_file("data/input.txt")+"\n----\n"\
          +open_file_pandas("data/input_pandas.txt")
    console_output(data)
    file_write("data/output.txt", data)



if __name__ == '__main__':
    main()

