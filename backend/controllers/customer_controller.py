from db_connection import get_db_connection
import pymysql.err
from utils.hasher import hash_password


class CustomerController:
	def create_customer(self, first_name, last_name, phone_number, email, password):
		password = hash_password(password)

		db = get_db_connection()
		cursor = db.cursor(pymysql.cursors.DictCursor)
		sql = """
			INSERT INTO Customer (first_name, last_name, phone_number, email, password) VALUES (%s, %s, %s, %s, %s)
		"""
		values = (first_name, last_name, phone_number, email, password)

		try:
			cursor.execute(sql, values)
			db.commit()
			return True
		except pymysql.err.IntegrityError as e:
			db.rollback()
			return False

	def get_all_customers(self):
		db = get_db_connection()
		cursor = db.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM Customer")
		results = cursor.fetchall()
		db.close()
		return results

	def get_customer_by_id(self, customer_id):
		db = get_db_connection()
		cursor = db.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM Customer WHERE id = %s", (customer_id,))
		result = cursor.fetchone()
		db.close()
		return result

	def update_customer(self, customer_id, **kwargs):
		fields = ("first_name", "last_name", "phone_number", "email", "password")
		updates = [f"{field} = %s" for field in kwargs.keys() if field in fields]

		if "password" in kwargs:
			kwargs["password"] = hash_password(kwargs["password"])

		if not updates:
			return False

		db = get_db_connection()
		cursor = db.cursor()
		sql = f"""UPDATE Customer SET {','.join(updates)} WHERE id = %s """
		values = list(kwargs.values()) + [customer_id]

		try:
			cursor.execute(sql, values)
			db.commit()
			return True
		except pymysql.err.IntegrityError as e:
			db.rollback()
			return False

	def delete_customer(self, customer_id):
		db = get_db_connection()
		cursor = db.cursor()
		sql = "DELETE FROM Customer WHERE id = %s"
		try:
			cursor.execute(sql, (customer_id,))
			db.commit()
			return True
		except pymysql.err.Error as e:
			db.rollback()
			return False


