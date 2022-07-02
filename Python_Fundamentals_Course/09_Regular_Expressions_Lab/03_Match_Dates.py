import re

pattern = r"\b(?P<Day>\d{2})(?P<Separator>[-.\/])(?P<Month>[A-Z][a-z]{2})(?P=Separator)(?P<Year>\d{4})\b"

dates = input()
valid_dates = [print(f"Day: {el.groupdict()['Day']}, Month: {el.groupdict()['Month']}, Year: {el.groupdict()['Year']}")
               for el in re.finditer(pattern, dates)]
