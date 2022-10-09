def check_len_of_str(password: str):
    dump = ''
    for i in password:
        if i not in dump:
            dump += i
    if len(dump) >= 3:
        return True
    else:
        return False


def is_acceptable_password(password: str) -> bool:
    if len(password) > 9 and 'password' not in password and 'PASSWORD' not in password and check_len_of_str(password):
        return True
    if len(password) > 6 and any(map(str.isdigit, password)) and any(map(str.isalpha, password)) \
            and 'password' not in password and 'PASSWORD' not in password and check_len_of_str(password):
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
assert is_acceptable_password("aaaaaa1") == False
assert is_acceptable_password("aaaaaabbbbb") == False
assert is_acceptable_password("aaaaaabb1") == True
assert is_acceptable_password("abc1") == False
assert is_acceptable_password("abbcc12") == True
assert is_acceptable_password("aaaaaaabbaaaaaaaab") == False
