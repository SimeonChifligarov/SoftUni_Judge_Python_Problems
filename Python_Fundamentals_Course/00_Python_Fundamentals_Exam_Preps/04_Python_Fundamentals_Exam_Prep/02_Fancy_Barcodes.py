#
import re

pattern = r"@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+"
pattern_digits = r"\d"

count_of_barcodes = int(input())

for _ in range(count_of_barcodes):
    current_barcode = input()
    validation_check = re.fullmatch(pattern, current_barcode)
    if validation_check:
        product_group = "00"
        digits_check = re.findall(pattern_digits, current_barcode)
        if digits_check:
            product_group = "".join(digits_check)
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")
