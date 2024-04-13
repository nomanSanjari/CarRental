from db_connection import get_db_connection
import pymysql.err


class RentalController:
	def create_rental(self, start_date, end_date, vehicle_id, employee_id, customer_id):
		db = get_db_connection()
		cursor = db.cursor()
		sql = """INSERT INTO Rental (start_date, end_date, vehicle_id, employee_id, customer_id, discount_id) VALUES (%s, %s, %s, %s, %s, %s)"""
		values = (start_date, end_date, vehicle_id, employee_id, customer_id)

		try:
			cursor.execute(sql, values)
			db.commit()
			return cursor.lastrowid
		except pymysql.err.IntegrityError as e:
			print(f"Error creating rental: {e}")
			db.rollback()
			return None

	def get_rental_by_id(self, rental_id):
		db = get_db_connection()
		cursor = db.cursor()
		sql = """SELECT * FROM Rental WHERE rental_id = %s"""
		values = (rental_id,)

		cursor.execute(sql, values)

		return cursor.fetchone()

	def get_all_rentals(self):
		db = get_db_connection()
		cursor = db.cursor()
		sql = """SELECT * FROM Rental"""

		cursor.execute(sql)

		return cursor.fetchall()

	def update_rental(self, rental_id, **kwargs):
		# Get modifiable fields
		fields = ("start_date", "end_date", "vehicle_id", "employee_id", "customer_id")
		updates = [f"{field} = %s" for field in kwargs.keys() if field in fields]

		if not updates:
			return False  # Nothing to update

		db = get_db_connection()
		cursor = db.cursor()
		sql = f"""UPDATE Rental SET {','.join(updates)} WHERE id = %s"""
		values = list(kwargs.values()) + [rental_id]

		try:
			cursor.execute(sql, values)
			db.commit()
			return True
		except pymysql.err.IntegrityError as e:
			print(f"Error updating rental: {e}")
			db.rollback()
			return False

	def delete_rental(self, rental_id):
		db = get_db_connection()
		cursor = db.cursor()
		sql = """DELETE FROM Rental WHERE id = %s"""
		values = (rental_id,)

		try:
			cursor.execute(sql, values)
			db.commit()
			return True
		except pymysql.err.IntegrityError as e:
			print(f"Error deleting rental: {e}")
			db.rollback()
			return False
