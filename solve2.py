import numpy as np
import jpeglib
import os
def count_zeros_in_4d_array(array):
    count = np.count_nonzero(array == 0)
    return count
zero_count_per_image = []

directory = "."

files = os.listdir(directory)


# Example 4D NumPy array (shape: (10, 20, 30, 40))
# Replace this with your actual 4D array
jpeg_files = [file for file in files if file.endswith(".jpg")]

for jpeg_file in jpeg_files:
    file_path = os.path.join(directory, jpeg_file)
    image = jpeglib.read_dct(file_path)
    array = image.Y
    zeros_count = count_zeros_in_4d_array(array)
    print("Number of zeros in  "+ str(file_path), zeros_count)
    zero_count_per_image.append(zeros_count)

