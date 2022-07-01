key = [int(el) for el in input().split()]

data = input()

while not data == "find":
    real_message = ""
    treasure_type = ""
    location = ""
    key_index = 0
    for index in range(len(data)):
        if key_index == len(key):
            key_index = 0
        real_message += chr(ord(data[index]) - key[key_index])
        key_index += 1

    start_index_type = real_message.index("&")
    real_message = real_message[start_index_type + 1:]
    end_index_type = real_message.index("&")
    treasure_type = real_message[:end_index_type]
    start_index_location = real_message.index("<")
    real_message = real_message[start_index_location + 1:]
    end_index_location = real_message.index(">")
    location = real_message[:end_index_location]
    print(f"Found {treasure_type} at {location}")
    data = input()
