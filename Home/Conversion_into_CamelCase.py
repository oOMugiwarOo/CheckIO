def to_camel_case(name: str) -> str:
    dump = ''
    for i in name.split('_'):
        dump += i.capitalize()
    return dump


print("Example:")
print(to_camel_case("my_function_name"))

assert to_camel_case("my_function_name") == "MyFunctionName"
assert to_camel_case("i_phone") == "IPhone"

# a = "my_function_name"
# print(a.split('_'))
# dump = ''
# for i in a.split('_'):
#     dump += i.capitalize()
# print(dump)


