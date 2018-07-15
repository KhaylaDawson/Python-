import os

file_location = input("Please enter a file loaction: ")
total_size = 0
home = file_location

def fileSpace():
  home = os.getcwd()
  path = os.path.join(home, file_location)
  os.chdir(path)
  file_size = [item for item in sample_directory if os.path.isdir(item)]












#main code
print("The total size for all files in", files, "is"
