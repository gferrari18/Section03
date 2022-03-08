# create an empty list
team = []

# ask the user for names.
# enter 'done' when complete
player = ''
while player != 'done':
    player = input('give me a player name: ')
    if player != 'done':
        team.append(player)

print('your team is: ')
for p in team:
    print("\t" + p)

team.reverse()
for p in team:
    print(p)

team.sort()
for p in team:
    print(p)


if "Gus" in  team:
    print("nice, im excited to play")
else: print("put me in coach, im ready")