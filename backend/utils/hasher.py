import bcrypt


def hash_password(plain_text_password):
	salt = bcrypt.gensalt()
	hashed_password = bcrypt.hashpw(plain_text_password.encode('utf-8'), salt)
	return hashed_password.decode('utf-8')  # Return as a string


def verify_password(plain_text_password, stored_hash):
	result = bcrypt.checkpw(plain_text_password.encode('utf-8'), stored_hash.encode('utf-8'))
	return result
