import random
import string

char_pool = string.ascii_letters + string.digits

def select(size=3, pool=char_pool):
	selection = random.choices(pool, k=size)
	return "".join(selection)

selection = []
collision_count = 0
loop_count = 0


size = 3
pool = [0,1,2]

while len(selection) < len(pool) ** size:
	i = select(size, pool)
	if i in selection:
		collision_count += 1
	else:
		selection.append(i)
	
	loop_count += 1

print(f"{collision_count}/{loop_count}")
print(len(selection))