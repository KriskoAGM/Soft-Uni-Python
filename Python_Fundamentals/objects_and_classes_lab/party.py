class Party:
    def __init__(self):
        self.people = []


party = Party()

while True:
    command_and_names = input()

    if command_and_names == "End":
        break
    party.people.append(command_and_names)

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")
