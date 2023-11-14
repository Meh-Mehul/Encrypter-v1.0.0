#decryptor
import re

from tkinter import *

root = Tk()
root.title('decrypter')
root.geometry("290x130+850+500")
no= Label(root,text=" ").grid(row=0, column= 0)
Lablehead1 = Label(root, text="Decrypter")
Lablehead1.grid(row=0, column=1)
Lablehead3 = Label(root, text="Enter Text: ")
Lablehead4 = Label(root, text="Enter Key: ")

Lablehead3.grid(row=3, column=1)
Lablehead4.grid(row=4, column=1)
lablehead2 = Label(root, text="By Mehul")
lablehead2.grid(row=0, column=2)
entryA= Entry(root, width= 20)
entryA.grid(row= 3,column=2)
entryB = Entry(root, width=20)
entryB.grid(row=4,column=2)

def encriptx():
	
	inputx = str(entryA.get())
	master_key_0 = str(entryB.get())
	W = int(master_key_0)
	input_0= inputx.upper()
	input_1 = re.sub(r'[^a-zA-Z]', ' ', input_0)

	input_list = list(input_1)
	n= len(input_0)
	str_final = ""


	for i in input_list:
	
		coverter = numero_source[i]
		k = int(coverter)
		M = (k - W + n)%26
		output= alphabet_source[M]
		n = n + 1
		str_final += output


	outputLabel0 = Label(root, text= "Ur Output: ").grid(row=21,column=1)
	outputLabel1 = Label(root, text= str_final).grid(row=21,column=2)
encrypt_it = Button(root, text="Decrypt", padx=15, pady=10, command=encriptx).grid(row=5, column=2)

numero_source = {
	 " " : 0,

	 "A" : 1
	 ,

	 "B" : 2
,
	 "C" : 3
,
	 "D" : 4
,
	 "E" : 5
,
	 "F" : 6
,
	 "G" : 7
,
	 "H" : 8
,
	 "I" : 9
,
	 "J" : 10
,
	 "K" : 11
,
	 "L" : 12
,
	 "M" : 13
,
	 "N" : 14
,
	 "O" : 15
,
	 "P" : 16
,
	 "Q" : 17
,
	 "R" : 18
,
	 "S" : 19
,
	 "T" : 20
,
	 "U" : 21
,
     "V" : 22
,
     "W" : 23
,
     "X" : 24
,
    "Y" : 25
,
     "Z" : 26



} 

alphabet_source = [ " " , "A" , "B" , "C" , "D", "E" , "F", "G", "H", "I", "J", "K", "L", "M", "N", "O" ,"P" ,"Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]






root.mainloop()