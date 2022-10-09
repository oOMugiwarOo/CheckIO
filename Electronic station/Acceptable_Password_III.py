def is_acceptable_password(password: str) -> bool:
    return True if len(password) > 6 and any(map(str.isdigit, password)) and any(map(str.isalpha, password)) else False


assert is_acceptable_password("short") == False
assert is_acceptable_password("muchlonger") == False
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False
