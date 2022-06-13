END_COMMAND = "END"

reservations = int(input())

reservation_codes_vip = set()
reservation_codes_regular = set()

for _ in range(reservations):
    current_code = input()
    if current_code[0].isdigit():
        reservation_codes_vip.add(current_code)
    else:
        reservation_codes_regular.add(current_code)

while True:
    arrived_guest = input()
    if arrived_guest == END_COMMAND:
        break
    if arrived_guest in reservation_codes_vip:
        reservation_codes_vip.remove(arrived_guest)
    if arrived_guest in reservation_codes_regular:
        reservation_codes_regular.remove(arrived_guest)

guests_not_arrived = len(reservation_codes_vip) + len(reservation_codes_regular)

print(guests_not_arrived)

for guest in sorted(reservation_codes_vip):
    print(guest)

for guest in sorted(reservation_codes_regular):
    print(guest)
