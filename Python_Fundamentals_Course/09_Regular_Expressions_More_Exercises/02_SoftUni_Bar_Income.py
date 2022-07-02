import re

pattern = r"%(?P<name>[A-Z][a-z]+)%([^\|\$\.%]+)?<(?P<product>\w+)>([^\|\$\.%]+)?\|([^\|\$\.%]+0-9)?(?P<count>\d+)([^\|\$\.%]+)?\|([^\|\$\.%0-9]+)?(?P<price>\d+(\.\d+)?)([^\|\$\.%]+)?\$"

data_as_line = input()

total_price = 0
while not data_as_line == "end of shift":
    matches = re.match(pattern, data_as_line)
    if matches:
        matches_as_dict = matches.groupdict()
        current_price = int(matches_as_dict['count']) * float(matches_as_dict['price'])
        total_price += current_price
        print(f"{matches_as_dict['name']}: {matches_as_dict['product']} - {current_price :.2f}")
        current_price = 0
    data_as_line = input()
print(f"Total income: {total_price :.2f}")
