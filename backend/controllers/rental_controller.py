from db_connection import get_db_connection
from utils.pricing import calculate_daily_price, calculate_weekly_price, calculate_price_after_discount
from utils.mailer import send_acceptance_email, send_rejection_email
import pymysql.err


class RentalController:
	def create_rental(self, start_date, end_date, vehicle_id, customer_id, discount_id, pricing_type):
		if discount_id is None:
			discount_id = None
		if discount_id == "":
			discount_id = None

		db = get_db_connection()
		cursor = db.cursor(pymysql.cursors.DictCursor)
		sql = """INSERT INTO Rental (start_date, end_date, vehicle_id, customer_id, discount_id, total_price, verified) VALUES (%s, %s, %s, %s, %s, %s, %s)"""

		verified = 0
		total_price = 0

		if pricing_type == "daily":
			total_price = calculate_daily_price(vehicle_id, start_date, end_date)
		elif pricing_type == "weekly":
			total_price = calculate_weekly_price(vehicle_id, start_date, end_date)

		total_price = calculate_price_after_discount(total_price, discount_id)

		values = (start_date, end_date, vehicle_id, customer_id, discount_id, total_price, verified)

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
		cursor = db.cursor(pymysql.cursors.DictCursor)
		sql = """SELECT * FROM Rental WHERE id = %s"""
		values = (rental_id,)

		cursor.execute(sql, values)

		return cursor.fetchone()

	def get_pending_rentals(self):
		db = get_db_connection()
		cursor = db.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM Rental WHERE verified = 0")
		results = cursor.fetchall()
		db.close()
		return results

	def get_all_rentals(self):
		db = get_db_connection()
		cursor = db.cursor(pymysql.cursors.DictCursor)
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

	def accept_rental(self, rental_id):
		db = get_db_connection()
		cursor = db.cursor()
		sql = """UPDATE Rental SET verified = 1 WHERE id = %s"""
		values = (rental_id,)

		customer_id = """SELECT customer_id FROM Rental WHERE id = %s"""
		cursor.execute(customer_id, values)
		db.commit()
		customer_id = cursor.fetchone()

		email = """SELECT email FROM Customer WHERE id = %s"""
		cursor.execute(email, customer_id)
		db.commit()
		email = cursor.fetchone()

		try:
			cursor.execute(sql, values)
			db.commit()
			send_acceptance_email(email, "Rental Accepted", "Your rental has been accepted")

			return True

		except pymysql.err.IntegrityError as e:
			print(f"Error verifying rental: {e}")
			db.rollback()
			return False

	def reject_rental(self, rental_id):
		db = get_db_connection()
		cursor = db.cursor()
		sql = """DELETE FROM Rental WHERE id = %s"""
		values = (rental_id,)

		customer_id = """SELECT customer_id FROM Rental WHERE id = %s"""
		cursor.execute(customer_id, values)
		db.commit()
		customer_id = cursor.fetchone()

		email = """SELECT email FROM Customer WHERE id = %s"""
		cursor.execute(email, customer_id)
		db.commit()
		email = cursor.fetchone()

		try:
			cursor.execute(sql, values)
			db.commit()
			send_rejection_email(email, "Rental Rejected", "Your rental has been rejected")

			return True
		except pymysql.err.IntegrityError as e:
			print(f"Error declining rental: {e}")
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
