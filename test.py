without_reminder = []
with_reminder = []
for x in range(0,10):
    for y in range(0,10):
        if x+y>9:
            with_reminder.append((x,y))
        else:
            without_reminder.append((x,y))


f = open("code.txt", "r")
for line in f:
    if line.startswith("turing.add_transition") and "default" not in line:
        first_div = line.split("[")
        second_div = first_div[1].split("]")
        for_change = second_div[0]
        for_change = for_change.replace("'", "")
        for_change = for_change.replace(",", "")
        for_change = for_change.replace(" ", "")
        for_change = "'" + for_change + "'"

        the_rest = line.split(":")
        line = first_div[0] + for_change + ":" + the_rest[1]
    print(line, end="")
f.close()
