from collections import deque

price_of_a_bullet = int(input())
gun_barrel_size = int(input())
bullets = [int(el) for el in input().split()]
locks = deque([int(el) for el in input().split()])
intelligence_value = int(input())

starting_bullets = len(bullets)
current_gun_barrel = gun_barrel_size

while locks and bullets:
    current_bullet = bullets.pop()
    current_lock = locks[0]

    if current_bullet <= current_lock:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")

    current_gun_barrel -= 1
    if current_gun_barrel == 0 and bullets:
        print("Reloading!")
        current_gun_barrel = gun_barrel_size

if not locks:
    remaining_bullets = len(bullets)
    money_earned = intelligence_value - (starting_bullets - remaining_bullets) * price_of_a_bullet
    print(f"{remaining_bullets} bullets left. Earned ${money_earned}")

else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
