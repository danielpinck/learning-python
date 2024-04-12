import keyboard, random

pipe_elements = ["\u2550", "\u2551", "\u2554", "\u2557", "\u255A", "\u255D"]

print(f"u2550 ist {'\u2550'}")
print(f"u2551 ist {'\u2551'}")
print(f"u2554 ist {'\u2554'}")
print(f"u2557 ist {'\u2557'}")
print(f"u255A ist {'\u255A'}")
print(f"u255D ist {'\u255D'}")



pipe_grid = [[],[],[],[],[],[]]
for i in range(0, len(pipe_grid)-1):
    for j in range(0, len(pipe_grid)-1):
        pipe_grid[i].append(pipe_elements[random.randint(0,len(pipe_elements)-1)])


# print(pipe_grid)
for i in range(len(pipe_grid)):
    print(*pipe_grid[i])