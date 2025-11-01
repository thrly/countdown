def time_to_seconds(time_string: str) -> int:
    # if user passes only and int, its seconds:
    if time_string.isdigit():
        return int(time_string)

    t_array = time_string.split(":")

    # TODO: ensure all elements are numbers or fail

    # if mm:ss
    if len(t_array) == 2:
        mm = int(t_array[0])
        ss = int(t_array[1])

        return (mm * 60) + ss

    # if hh:mm:ss
    elif len(t_array) == 3:

        hh = int(t_array[0])
        mm = int(t_array[1])
        ss = int(t_array[2])
        return (hh * 3600) + (mm * 60) + ss

    else:
        print("Enter time in seconds (int) or [hh:]mm:ss format")
        return 0


#
#
# print(time_to_seconds("04:30"))
# print(time_to_seconds("30"))
# print(time_to_seconds("1:04:30"))
# print(time_to_seconds("test:0"))
