import os.path

my_file = "famous_quotes.txt"

if os.path.isfile(my_file):
    print(f"The file {my_file} exists")
else:
    print(f"The file {my_file} doesn't exist")

