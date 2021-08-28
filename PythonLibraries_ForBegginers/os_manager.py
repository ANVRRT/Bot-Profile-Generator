import os
import pandas as pd

class OSManager:

    def __init__(self):
        pass

    def clear_console_log():
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_file_size(path):
        return (os.path.getsize(path))
    
    def open_file(path):
        file = open(path,"a")
        return file

    def file_is_empty(path):
        fileSize = OSManager.get_file_size(path)
        if fileSize == 0:
            return True
        else:
            return False

    def create_directory(path):

        os.makedirs(os.path.dirname(path), exist_ok = True)

    def create_file(path, output = False): #Returns an opened file

        OSManager.create_directory(path)
        
        file = open(path,"a")


        if output == True:
            return file
        else:
            file.close()
        # return (os.path.getsize(f"{path}"))
    
    def open_pandas_csv_file(path):

        OSManager.create_file(path)

        pandasFile = pd.read_csv(path)
        
        return pandasFile
