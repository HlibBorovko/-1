from fileinput import filename
import csv
import sys
print("Группа 2")
filename = "C:\Users\Admin\Desktop 2.txt"
text_file = open("C:\Users\Admin\Desktop 2.txt","r")
reader=csv.reader(text_file,delimiter="t")
for row in  reader:
    print(row)
text_file.close()



import csv
import sys
print("Группа 3")
filename = "C:\Users\Admin\Desktop 3.txt"
text_file = open("C:\Users\Admin\Desktop 3.txt","r")
reader=csv.reader(text_file,delimiter="t")
for row in  reader:
    print(row)
text_file.close()



import csv
import sys
print("Группа 4")
filename = "C:\Users\Admin\Desktop 4.txt"
text_file = open("C:\Users\Admin\Desktop 4.txt","r")
reader=csv.reader(text_file,delimiter="t")
for row in  reader:
    print(row)
text_file.close()
