# How to open a File

import os

current_directory = os.getcwd()
print(current_directory)


folder_path = "C:\Users\MK System\PycharmProjects\Python_Learning\Modules & Files\open_files.py"

result = os.listdir(folder_path)
print(result)