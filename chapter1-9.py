import os
import csv

file_path = os.path.join("Users", "mizukoshinarumi", "workspace", "python_workspace", "python_self_taught_programmer", "file.txt")

with open("/" + file_path, "w", encoding="utf-8") as f:
    f.write("Hi from Python!")

my_list = []
with open("/" + file_path, "r", encoding="utf-8") as f:
    my_list.append(f.read())

print(my_list)

with open("/" + file_path, "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["one", "two", "three"])
    w.writerow(["four", "five", "six"])

with open("/" + file_path, "r", encoding="utf-8") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))