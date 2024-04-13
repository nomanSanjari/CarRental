from db_connection import get_db_connection
import pymysql.err


def calculate_weekly_price(vehicle_id, start_date, end_date):
	db = get_db_connection()
	cursor = db.cursor()
	sql = """SELECT weekly_rate FROM Vehicle WHERE id = %s"""
	values = (vehicle_id,)

	cursor.execute(sql, values)
	result = cursor.fetchone()
	db.close()

	if not result:
		return None

	weekly_rate = result[0]
	days = (end_date - start_date).days
	weeks = days // 7
	remainder_days = days % 7

	return weeks * weekly_rate + remainder_days * (weekly_rate / 7)


def calculate_daily_price(vehicle_id, start_date, end_date):
	db = get_db_connection()
	cursor = db.cursor()
	sql = """SELECT daily_rate FROM Vehicle WHERE id = %s"""
	values = (vehicle_id,)

	cursor.execute(sql, values)
	result = cursor.fetchone()
	db.close()

	if not result:
		return None

	daily_rate = result[0]
	days = (end_date - start_date).days

	return days * daily_rate


def calculate_price_after_discount(price_before_discount, discount_id):
	db = get_db_connection()
	cursor = db.cursor()
	sql = """SELECT discount_percentage FROM Discount WHERE id = %s"""
	values = (discount_id,)

	cursor.execute(sql, values)
	result = cursor.fetchone()
	db.close()

	if not result:
		return None

	discount_percentage = result[0]
	discounted_amount = price_before_discount * discount_percentage / 100

	return price_before_discount - discounted_amount
