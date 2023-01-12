#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import configparser

import mysql.connector

class MyDatabase:

	__single_instance = None

	@classmethod
	def single_instance(cls):
		if not cls.__single_instance:
			cls.__single_instance = cls()

		return cls.__single_instance

	def create_conn_obj(self):	
		try:
			cfg = configparser.ConfigParser()
			BASE_DIR = os.path.dirname(os.getcwd())
			file_path = os.path.join(BASE_DIR,'model/config.ini')
			cfg.read(file_path)
			host    = cfg['Database']['host']
			user    = cfg['Database']['user']
			passwd  = cfg['Database']['password']
			dbase   = cfg['Database']['database']

			conn = mysql.connector.connect(host = host,
										   user = user,
										   password = passwd,
										   database = dbase)
			return conn
			
		except mysql.connector.errors.DatabaseError as e:
			print(e)

	def get_data(self, sql, crsor):

		if sql and crsor:
			try:
				crsor.execute(sql)
			except mysql.connector.Error as e:
				print(e.msg)
			else:
				info = crsor.fetchone()
				# info = crsor.fetchmany() / crsor.fetchall()
				return info


	def create_table(self, sql, crsor):

		if sql and crsor:
			try:
				crsor.execute(sql)
			except mysql.connector.Error as e:
				if e.errno == mysql.connector.errorcode.ER_CANT_CREATE_TABLE:
					print(str(e))
				else:
					print(e.msg)
			else:
				print(crsor.info())
				print(crsor.column_names)

	def delete_data(self, sql, crsor):

		if sql and crsor:
			try:
				crsor.execute(sql)
			except mysql.connector.Error as e:
				if e.errno == mysql.connector.errorcode.ER_CANT_CREATE_TABLE:
					print(str(e))
				else:
					print(e.msg)
			else:
				print(crsor.info())
				print(crsor.rowcount)


	def insert_or_update_table(self, sql, conn, crsor):

		if sql and crsor:
			try:
				crsor.execute(sql)
			except mysql.connector.Error as e:
				print(e.msg)
			else:
				conn.commit()
				print(crsor.info())
				print(crsor.rowcount)

	
				
		
			
		

			
