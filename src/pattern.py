
stars=[]
for i in range(1,6,1):
    stars.append("*")
    print(" ".join(stars))
while len(stars)>0:
    stars.pop()
    print(" ".join(stars))


# Print the pattern
