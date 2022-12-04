#!/usr/bin/env python
import hashlib
import os
#This is a program to generate a securely hashed and salted password
#This password is stored securely in 'pass.txt'
password = input("Enter secure password: ")
salt = os.urandom(32)
key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
#Password is salted
storage = salt + key
#Printing the result purely for visual demonstration
print(storage)
#Password is stored in file
f = open('pass.txt', 'wb')
f.write(storage)
f.close()
f = open('pass.txt', 'rb')
salty = f.read()
print(salty)