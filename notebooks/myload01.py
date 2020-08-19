import os
import numpy as np
import pandas as pd 

def disp_files_folder(folder_path):
        print("\n Files in the folders are: \n")
        for dirname, _, filenames in os.walk(folder_path):
                for filename in filenames:
                        print(os.path.join(dirname, filename))
        print("\n")
        return

def load_csv(file_name):
        df = pd.read_csv(file_name)
        return df

if __name__ == "__main__":
    folder_path = 'C:\\Users\\sabbi\\Dropbox\\Darryl James\\Mendeley_library\\JetEntrainment\\Selective\\Qualifying_docs\\SW_Python\\input' 
    disp_files_folder(folder_path)
    file_name = 'C:\\Users\\sabbi\\Dropbox\\Darryl James\\Mendeley_library\\JetEntrainment\\Selective\\Qualifying_docs\\SW_Python\\input\\single.csv' 
    data_single = load_csv(file_name)

  

