def is_acceptable_password(password: str) -> bool:

    # return True if len(password) > 6 and any(map(str.isdigit, password)) and any(map(str.isalpha, password)) else False
    if len(password) > 9:
        return True
    elif len(password) > 6 and any(map(str.isdigit, password)) and any(map(str.isalpha, password)):
        return True
    else:
        return False

assert is_acceptable_password("short") == False
assert is_acceptable_password("short54") == True
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("notshort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False
assert is_acceptable_password("12345678910") == True

# a = '12345678910'
# if len(a) > 9:
#     print('Yes')
# elif len(a) > 6 and any(map(str.isdigit, a)) and any(map(str.isalpha, a)):
#     print('Yes')
# else:
#     print('No')
