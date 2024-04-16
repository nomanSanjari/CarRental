from db_connection import get_db_connection
import pymysql.err
from utils.hasher import hash_password


class AuthController():
	def login_customer(self, email, password):
		db = get_db_connection()
		cursor = db.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM Customer WHERE email = %s", (email,))
		result = cursor.fetchone()
		db.close()

		if result and result["password"] == hash_password(password):
			return result
		else:
			return False

	def login_employee(self, email, password):
		db = get_db_connection()
		cursor = db.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM Employee WHERE email = %s", (email,))
		result = cursor.fetchone()
		db.close()

		if result and result["password"] == hash_password(password):
			return result
		else:
			return False
