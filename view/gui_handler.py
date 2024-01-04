#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import Toplevel,Frame, Tk, Label, Button, Entry, StringVar
from tkinter import messagebox
import string

class Login:
	def __init__(self):
		#self.root = root
		self.user = None
		self.level = None
		self.create()
		
	def create(self):
		self.level = Tk()
		self.level.geometry("300x100")
		self.level.title("Login")
		
		usr_label = Label(self.level, text="Enter Username")
		pwd_label = Label(self.level, text="Enter Password")

		usr_var   = StringVar()
		pwd_var   = StringVar()
		
		self.usr_entry = Entry(self.level,textvariable=usr_var) 
		self.pwd_entry = Entry(self.level,textvariable=pwd_var, show="*")

		usr_label.grid(row=0, column=0, sticky="w")
		pwd_label.grid(row=1, column=0, sticky="w")
		self.usr_entry.grid(row=0, column=1, sticky="e", columnspan=2)
		self.pwd_entry.grid(row=1, column=1, sticky="e", columnspan=2)

		btn_submit = Button(self.level, command=self.verify, text="Sign In")
		btn_submit.grid(row=4, rowspan=2, column=1, columnspan=3, sticky="nsew")
		
		self.level.mainloop()
	
	def verify(self):

		user = self.usr_entry.get()
		pwd = self.pwd_entry.get()

		if user and pwd:
			if len(pwd) < 8 or len(pwd) > 15:
				messagebox.showerror("Password Error",
									 "Length of Password should be between 8 and 15")
			elif not any(letter.isupper() for letter in pwd):
				messagebox.showerror("Password Error",
									 "Password must have atleast one upper case")
			elif not any(letter.islower() for letter in pwd):
				messagebox.showerror("Password Error",
									 "Password must have atleast one lowercase")
			elif not any(letter.isdigit() for letter in pwd):
				messagebox.showerror("Password Error",
									 "Password must have atleast one numerical value")

			elif not any(letter in string.punctuation for letter in pwd):
				messagebox.showerror("Password Error",
									 "Password must have atleast one special character")
			else:
				self.redirect_dashboard({'user': user, 'pwd': pwd})
		else:
			messagebox.showerror("Password Error",
								 "Error in matching either username or password")

	def redirect_dashboard(self, data):
		self.user = data.get('user')
		print(self.user)
