import random
import re


print("Enter A puppy name")
A = input()
print("Enter B puppy name")
B = input()

pup2 = "[Gg]ellar|[Bb]ully|[Bb]lackhead|[Pp]rincess|[Tt]hanos|[Nn]inja"

if A==B:
	print("Enter a different puppy:")
elif re.search(pup2,A):
	print(A)
elif re.search(pup2,B):
	print(B)
else:
	print("And the grand winner is: ")
	print(random.choice(A,B))
