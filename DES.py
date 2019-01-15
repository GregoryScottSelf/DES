
#-------------------------------------------------------------------------------
#Name: Greg Self
#Project: DES Encrytion and Decrytion
#Description- This is a program that demonstrates how DES is executed in python.
#The user is able to enter in a piece of text and it is encrypted
#The encrypted text is printed first
#Followed by the decrypted text

# Please note to run this program you must install Crypto.Cipher Library
#-------------------------------------------------------------------------------
from Crypto.Cipher import DES
storeDES = DES.new('12345678', DES.MODE_ECB)
text = raw_input("Enter a message to be enctypted:")
#finding length of input
store=len(text)
#logic for offset
#total slots to fill is 8, will be filled with blank spaces as fillers
offset=store % 8
filler=8-offset
#newtext = text
if offset!= 0:
    i=0
    while i<filler:
        text=text+str(" ")
        i=i+1

cipher_text = storeDES.encrypt(text)
print("This is the cipher text:")
print(cipher_text)
storeDES.decrypt(cipher_text)
print("This is the message decrypted:")
print(text)

