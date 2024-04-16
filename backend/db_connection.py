import pymysql

# Replace placeholders with your actual database credentials
db_config = {
	'host': '127.0.0.1',
	'user': 'root',
	'password': 'root',
	'database': 'CarRentalDB'
}


# Function to establish and return a database connection
def get_db_connection():
	try:
		connection = pymysql.connect(**db_config)
		return connection
	except pymysql.err.OperationalError as e:
		print(f"Connection error: {e}")