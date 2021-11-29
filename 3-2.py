from fileinput import filename
import csv
import sys
print("Группа2")
 filename = "C:\Users\Admin\Desktop\Группа 2.txt"
text_file = open ("C:\Users\Admin\Desktop\Группа 2.txt","r")
reader=csv.reader(text_file,delimiter="t")
def sortByAlphabet(inputStr):
        return inputStr[0]
for str in reader:
 print (str)
text_file.close()
© 2021 GitHub, Inc.
Terms
Pr
