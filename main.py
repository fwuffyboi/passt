#use 'pip import mycrypto' in the shell before use

import mycrypto
import random
from random import randint
import random, os
from PIL import Image
import time
import colorama
from colorama import Fore, Back, Style
import sys


#variable stuff we need

inp = 'string_empty'
version = '2.0.0'
status_release = 'none - none'
zero = '00'
one = '01'
two = '02'
three = '03'



title = ('''
$$$$$$$\                                 $$\     
$$  __$$\                                $$ |    
$$ |  $$ |$$$$$$\   $$$$$$$\  $$$$$$$\ $$$$$$\   
$$$$$$$  |\____$$\ $$  _____|$$  _____|\_$$  _|  
$$  ____/ $$$$$$$ |\$$$$$$\  \$$$$$$\    $$ |    
$$ |     $$  __$$ | \____$$\  \____$$\   $$ |$$\ 
$$ |     \$$$$$$$ |$$$$$$$  |$$$$$$$  |  \$$$$  |
\__|      \_______|\_______/ \_______/    \____/                                                 

 01110000 01100001 01110011  01110011    01110100
                                                                  
 112      97       115       115         116    
 ''')

def encrypt():
	os.system('clear')
	print('enter message to encrypt')
	print('enter 00 to cancel')
	inp = input()
	print('input recieved')
	time.sleep(1)
	print('calculating..')
	time.sleep(0.2)
	print(inp)
	if (inp) == (zero):
		sys.exit()
	
	no_odd = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71,73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
	t1 = random.choice(no_odd)
	t2 = random.choice(no_odd)
	os.system('clear')
	print(Fore.BLUE, 't1 is ')
	print(Style.RESET_ALL)
	print(t1)
	print(Fore.BLUE, 't2 is ')
	print(Style.RESET_ALL)
	print(t2)

	mycrypto.Affine_encode((inp),(t1),(t2))
	time.sleep(2)
	print('''Press the enter key to continue.
	Make sure you also remember the 't1' and 't2' codes.
	These will be important when decoding!

	
	''')
	input()
	choose()


def decrypt():
	dec1 = ''
	dec2 = ''

	print('''
	dec1 = ''
	dec2 = '' ''')
	os.system('clear')
	print('enter message to decrypt')
	print('enter 00 to cancel')
	inp = input()
	print('enter t1')
	(dec1) = input()
	print(dec1)
	os.system('clear')
	print('enter t2')
	(dec2) = input()
	print(dec2) 
	print('input recieved')
	time.sleep(1)
	print('calculating..')
	time.sleep(0.2)
	print(inp)
	if (inp) == (zero):
		sys.exit()
	
	os.system('clear')

	mycrypto.Affine_decode((inp),(dec1),(dec2))
	time.sleep(2)
	print('Press the enter key to continue.')
	input()
	choose()

def info():
	os.system('clear')
	print('''
	MyCrypto python package developed by 

	@ZhiShi
	
	press enter for the next page.  page 1
	 ''')

	input()

	os.system('clear')
	print('''
	developers

	@fluffywolff
	
	press enter for the next page.  page 2
	 ''')

	input() 
	os.system('clear')

	print('''
	python packages used:

	--mycrypto

	--colorama

	--random

	--os

	--time
	
	--sys

	press enter for the next page.  page 3
	 ''')

	input() 
	os.system('clear')

	print(''' 
	 end of credits
	 
	 press enter to go to menu
	 ''')

	input() 
	choose()

def choose():
	os.system('clear')
	print(''' 
	

[00]  ---  terminate program
[01]  ---  encrypt 
[02]  ---  decrypt
[03]  ---  information
	
	
	
''')
	todo = input()
	if (todo) == (zero):
		print('program terminated')
		sys.exit
	
	if (todo) == (one):
		encrypt()
	
	if (todo) == (two):
		decrypt()
	
	if (todo) == (three):
		info()
	else:
		choose()

# actuall code

#whattodo = input('''
#Enter 0 to encryt
#Enter 1 to decrypt

#Made by @Fluffywolff on replit.com
#title: Cryptography Test
#Last edits made: -------------

#Credit to the developers of the 'mycrypto' python package

#''')


print(Fore.BLUE + (title))

time.sleep(0.1)
print('version: ')
print(version)

print('\n')


time.sleep(5)


os.system('clear')
print('made')
time.sleep(0.2)
os.system('clear')
print('made by')
time.sleep(0.2)
os.system('clear')
print('made by: @fluffy')
time.sleep(0.2)
os.system('clear')
print('made by: @fluffyWolff')
time.sleep(2)
print('on')
os.system('clear')
print('made by: @fluffyWolff')
print('on re')
time.sleep(0.2)
os.system('clear')
print('made by: @fluffyWolff')
print('on repli')
time.sleep(0.2)
os.system('clear')
print('made by: @fluffyWolff')
print('on replit.')
time.sleep(0.2)
os.system('clear')
print('made by: @fluffyWolff')
print('on replit.com')
time.sleep(2)
os.system('clear')
choose()
