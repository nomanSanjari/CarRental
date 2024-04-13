from db_connection import get_db_connection
import pymysql.err
from utils.hasher import hash_password


class VehicleController():
	def create_vehicle(self, vin, make, model, vehicle_class, weekly_rate, daily_rate, odometer_reading, drive_train, is_available):
		db = get_db_connection()
		cursor = db.cursor()
		sql = """INSERT INTO Vehicle (vin, make, model, vehicle_class, weekly_rate, daily_rate, odometer_reading, drive_train, is_available) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
		values = (vin, make, model, vehicle_class, weekly_rate, daily_rate, odometer_reading, drive_train, is_available)
		try:
			cursor.execute(sql, values)
			db.commit()
			return True
		except pymysql.err.IntegrityError as e:
			print(f"Error creating vehicle: {e}")
			db.rollback()
			return False

	def get_all_vehicles(self):
		db = get_db_connection()
		cursor = db.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM Vehicle")
		results = cursor.fetchall()
		db.close()
		return results

	def get_vehicle_by_id(self, vehicle_id):
		db = get_db_connection()
		cursor = db.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM Vehicle WHERE id = %s", (vehicle_id,))
		result = cursor.fetchone()
		db.close()
		return result

	def get_vehicle_by_vin(self, vin):
		db = get_db_connection()
		cursor = db.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM Vehicle WHERE vin = %s", (vin,))
		result = cursor.fetchone()
		db.close()
		return

	def update_vehicle(self, vehicle_id, **kwargs):
		fields = ("vin", "make", "model", "vehicle_class", "weekly_rate", "daily_rate", "odometer_reading", "drive_train", "is_available")
		updates = [f"{field} = %s" for field in kwargs.keys() if field in fields]

		if not updates:
			return False

		db = get_db_connection()
		cursor = db.cursor()
		sql = f"""UPDATE Vehicle SET {','.join(updates)} WHERE id = %s """
		values = list(kwargs.values()) + [vehicle_id]

		try:
			cursor.execute(sql, values)
			db.commit()
			return True
		except pymysql.err.IntegrityError as e:
			print(f"Error updating vehicle: {e}")
			db.rollback()
			return False

	def delete_vehicle(self, vehicle_id):
		db = get_db_connection()
		cursor = db.cursor()
		sql = "DELETE FROM Vehicle WHERE id = %s"
		try:
			cursor.execute(sql, (vehicle_id,))
			db.commit()
			return True
		except pymysql.err.Error as e:
			print(f"Error deleting vehicle: {e}")
			db.rollback()
			return False
