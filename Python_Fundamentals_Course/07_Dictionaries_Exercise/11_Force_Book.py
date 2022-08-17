force_user_side = input()

force_sides_dict = {}
unique_force_users = []
while not force_user_side == "Lumpawaroo":
    split_data_bybar = force_user_side.split(" | ")
    if len(split_data_bybar) > 1:
        force_side = split_data_bybar[0]
        force_user = split_data_bybar[1]
        if force_user not in unique_force_users:
            if force_side not in force_sides_dict:
                force_sides_dict[force_side] = []
            if force_user not in force_sides_dict[force_side]:
                force_sides_dict[force_side].append(force_user)
                unique_force_users.append(force_user)

    elif len(split_data_bybar) == 1:
        split_data_byarrow = force_user_side.split(" -> ")
        force_user = split_data_byarrow[0]
        force_side = split_data_byarrow[1]
        if force_side not in force_sides_dict:
            force_sides_dict[force_side] = []
        for side, users in force_sides_dict.items():
            if force_user in users:
                force_sides_dict[side].remove(force_user)
        force_sides_dict[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    force_user_side = input()

# At that point you should print each force side, ordered descending by forceUsers count,
# than ordered by name. For each side print the forceUsers, ordered by name.

# sorted_forces_dict = sorted(force_sides_dict.items(), key=lambda x: (-len(x[1]), x[0]))
#
# for side, members in sorted_forces_dict:
#     if members:
#         print(f"Side: {side}, Members: {len(members)}")
#         for mem in sorted(members):
#             print(f"! {mem}")

for side, members in force_sides_dict.items():
    if members:
        print(f"Side: {side}, Members: {len(members)}")
        for mem in members:
            print(f"! {mem}")

# # Solution 2
# force_user_side = input()
#
# force_sides_dict = {}
#
# while not force_user_side == "Lumpawaroo":
#     split_data_bybar = force_user_side.split(" | ")
#     if len(split_data_bybar) > 1:
#         force_side = split_data_bybar[0]
#         force_user = split_data_bybar[1]
#         if force_user not in force_sides_dict:
#             force_sides_dict[force_user] = force_side
#
#     else:
#         split_data_byarrow = force_user_side.split(" -> ")
#         force_user = split_data_byarrow[0]
#         force_side = split_data_byarrow[1]
#         force_sides_dict[force_user] = force_side
#         print(f"{force_user} joins the {force_side} side!")
#     force_user_side = input()
#
# final_dict = {}
# for user, side in force_sides_dict.items():
#     if side not in final_dict:
#         final_dict[side] = []
#     final_dict[side].append(user)
#
# sorted_final_dict = sorted(final_dict.items(), key=lambda x: (-len(x[1]), x[0]))
#
# for side, members in sorted_final_dict:
#     if members:
#         print(f"Side: {side}, Members: {len(members)}")
#         for mem in sorted(members):
#             print(f"! {mem}")
