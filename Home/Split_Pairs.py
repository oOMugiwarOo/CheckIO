from typing import Iterable
import re


def split_pairs(text: str) -> Iterable[str]:
    result = re.findall(r'\w\w', text)
    if len(text) % 2 == 0:
        return result
    else:
        result.append(text[-1] + '_')
        return result


print("Example:")
print(list(split_pairs("abcd")))

assert list(split_pairs("abcd")) == ["ab", "cd"]
assert list(split_pairs("abc")) == ["ab", "c_"]
assert list(split_pairs("abcdf")) == ["ab", "cd", "f_"]
assert list(split_pairs("a")) == ["a_"]
assert list(split_pairs("")) == []
