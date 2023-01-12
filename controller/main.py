#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Pyp.model import connection
from Pyp.view import gui_handler

if __name__ == "__main__":
	
	db = connection.MyDatabase.single_instance()
	conn = db.create_conn_obj()
	print(conn)

	gui_handler.Login()
	

	


