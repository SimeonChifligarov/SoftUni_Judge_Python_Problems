# Create a class Party that only has an attribute called people. The __init__ method should not accept any parameters.
# You will be given names of people (on separate lines) until you receive the command "End".
# Use the created class to solve this problem. After you receive the end command print 2 lines:
# •	"Going: {people}" - the people should be separated by comma and space ", "
# •	"Total: {total_people_going}"

class Party:
    def __init__(self):
        self.people = []


name = input()
my_party = Party()
while not name == "End":
    my_party.people.append(name)
    name = input()

total_people_going = len(my_party.people)
print(f"Going: {', '.join(my_party.people)}")
print(f"Total: {total_people_going}")
