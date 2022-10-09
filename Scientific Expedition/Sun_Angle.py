from typing import Union


def sun_angle(time: str) -> Union[int, str]:
    b = time.split(':')
    if int(b[0]) >= 18 and int(b[1]) > 0 or int(b[0]) < 6:
        return "I don't see the sun!"
    return ((int(b[0]) - 6) * 60 + int(b[1])) * 0.25


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    assert sun_angle("07:00") == 15
    assert sun_angle("18:01") == "I don't see the sun!"
