def is_acceptable_password(password: str) -> bool:
    if len(password) > 9 and 'password' not in password and 'PASSWORD' not in password:
        return True
    elif len(password) > 6 and any(map(str.isdigit, password)) and any(map(str.isalpha, password)) and 'password' not in password and 'PASSWORD' not in password:
        return True
    else:
        return False


assert is_acceptable_password("short") == False
assert is_acceptable_password("short54") == True
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False
assert is_acceptable_password("12345678910") == True
assert is_acceptable_password("password12345") == False
assert is_acceptable_password("PASSWORD12345") == False
assert is_acceptable_password("pass1234word") == True
