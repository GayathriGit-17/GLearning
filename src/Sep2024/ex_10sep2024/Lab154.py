import os

try:
    full_path =os.getcwd()
    print(full_path)
    file = open('/Users/G3_sh/Desktop/amazon gift card.txt', 'r')  # File not found error
    print(file.read())
except FileNotFoundError as fnf:
    print("File not found please check the path or create a file")
finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)
