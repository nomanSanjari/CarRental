from db_connection import get_db_connection
import pymysql.err


class DiscountController:
	def create_discount(self, discount_type, discount_percentage):
		db = get_db_connection()
		cursor = db.cursor()
		sql = """INSERT INTO Discount (discount_type, discount_percentage) VALUES (%s, %s)"""
		values = (discount_type, discount_percentage)
		try:
			cursor.execute(sql, values)
			db.commit()

			last_inserted_id = cursor.lastrowid
			fetch_sql = """SELECT * FROM Discount WHERE id = %s"""
			cursor.execute(fetch_sql, (last_inserted_id,))

			return cursor.fetchone()

		except pymysql.err.IntegrityError as e:
			print(f"Error creating discount: {e}")
			db.rollback()
			return None

	def get_all_discounts(self):
		db = get_db_connection()
		cursor = db.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM Discount")
		results = cursor.fetchall()
		db.close()
		return results

	def get_discount_by_id(self, discount_id):
		db = get_db_connection()
		cursor = db.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM Discount WHERE id = %s", (discount_id,))
		result = cursor.fetchone()
		db.close()
		return result

	def update_discount(self, discount_id, **kwargs):
		fields = ("discount_type", "discount_percentage")
		updates = [f"{field} = %s" for field in kwargs.keys() if field in fields]

		if not updates:
			return False

		db = get_db_connection()
		cursor = db.cursor()
		sql = f"""UPDATE Discount SET {','.join(updates)} WHERE id = %s """
		values = list(kwargs.values()) + [discount_id]

		try:
			cursor.execute(sql, values)
			db.commit()
			return True
		except pymysql.err.IntegrityError as e:
			print(f"Error updating discount: {e}")
			db.rollback()
			return False

	def delete_discount(self, discount_id):
		db = get_db_connection()
		cursor = db.cursor()
		sql = """DELETE FROM Discount WHERE id = %s"""
		try:
			cursor.execute(sql, (discount_id,))
			db.commit()
			return True
		except pymysql.err.Error as e:
			print(f"Error deleting discount: {e}")
			db.rollback()
			return False
