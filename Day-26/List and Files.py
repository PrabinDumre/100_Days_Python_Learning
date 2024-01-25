# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[10]:9.50

# Change "living room" to "chill zone"
areas[5]="chill zone"

print(areas)

#File 

with open("prabin.txt") as f:
    a = f.read(12)
    print(a)
# f = open("prabin.txt")
# print(f.readline())
# f.close()