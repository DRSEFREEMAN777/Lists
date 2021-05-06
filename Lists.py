#Here I set up lists. They can contain many different types of data.
alst = [0, "5", "Four", 4]
blst = ["Seven", 2, 88]

#Here I print the lists.
print(len(alst))
print(len(blst))

#Here I loop or iterate through the lists and print each element of them.
for elem in alst:
    print(elem)

for elem2 in blst:
    print(elem2)

#Here I create a new list add add to it by looping through the first 2 lists
newlst = []

for elem in alst:
    newlst.append(elem)
for elem2 in blst:
    newlst.append(elem2)

print(newlst)

#Here I show how to index a list:

print(alst[1])

print(blst[1])


##CODE CHALLENGE: CREATE THREE LISTS. CREATE A FOURTH LIST WITH NO ELEMENTS. USING LOOPS, ADD THE ELEMENTS OF ALL THREE LISTS TO THE FOURTH LIST. PUSH THIS TO YOUR REPO.
alist =[ "orange", "blue", "red"]
blist = ["First", 2, 5]
clist =["Gold", "Silver", 5]
dlist =[] #No Element empty list

# loops

for elem in alist:
    dlist.append(elem)

for elem2 in blist:
    dlist.append(elem2)

for elem3 in clist:
    dlist.append(elem3)


print(dlist)