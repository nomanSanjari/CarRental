from db_connection import get_db_connection
import pymysql.err
from utils.hasher import hash_password


class EmployeeController:
	def create_employee(self, first_name, last_name, phone_number, email, password):
		password = hash_password(password)

		db = get_db_connection()
		cursor = db.cursor(pymysql.cursors.DictCursor)
		sql = """
			INSERT INTO Employee (first_name, last_name, phone_number, email, password) VALUES (%s, %s, %s, %s, %s)
		"""
		values = (first_name, last_name, phone_number, email, password)

		try:
			cursor.execute(sql, values)
			db.commit()
			return True
		except pymysql.err.IntegrityError as e:
			db.rollback()
			return False

	def get_all_employees(self):
		db = get_db_connection()
		cursor = db.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM Employee")
		results = cursor.fetchall()
		db.close()
		return results

	def get_employee_by_id(self, employee_id):
		db = get_db_connection()
		cursor = db.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM Employee WHERE id = %s", (employee_id,))
		result = cursor.fetchone()
		db.close()
		return result

	def update_employee(self, employee_id, **kwargs):
		fields = ("first_name", "last_name", "phone_number", "email", "password")
		updates = [f"{field} = %s" for field in kwargs.keys() if field in fields]

		if "password" in kwargs:
			kwargs["password"] = hash_password(kwargs["password"])

		if not updates:
			return False

		db = get_db_connection()
		cursor = db.cursor()
		sql = f"""UPDATE Employee SET {','.join(updates)} WHERE id = %s """
		values = list(kwargs.values()) + [employee_id]

		try:
			cursor.execute(sql, values)
			db.commit()
			return True
		except pymysql.err.IntegrityError as e:
			db.rollback()
			return False

	def delete_employee(self, employee_id):
		db = get_db_connection()
		cursor = db.cursor()
		sql = "DELETE FROM Customer WHERE id = %s"
		try:
			cursor.execute(sql, (employee_id,))
			db.commit()
			return True
		except pymysql.err.Error as e:
			db.rollback()
			return False


