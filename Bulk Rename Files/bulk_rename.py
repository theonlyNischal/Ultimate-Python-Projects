import os
import sys
import random
import string

chars_and_numbers = string.ascii_letters + string.digits

def rename(directory):
    print("-------------------------------------------")
    print("Directory: {}".format(directory))
    print("--------------------------------------------")

    for fileName in os.listdir(directory):
        title, ext = os.path.splitext(os.path.basename(fileName))
        random_title = "".join(random.sample(chars_and_numbers, 7))
        os.rename(directory + "/" + fileName, directory + "/" + random_title + ext)


directory = sys.argv[1]

rename(directory)