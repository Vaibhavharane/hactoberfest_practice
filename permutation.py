def permutation(list):
    # for empty list
    if len(list) == 0:
        return []

    # for only 1 element
    if len(list) == 1:
        return [list]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(list)):
        m = list[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        copy_list = list[:i] + list[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in permutation(copy_list):
            l.append([m] + p)
    print("Permutations for your list are :",l)
    return l


# Driver program to test above function
list=[]
n=int(input("Enter number of elements :"))
for i in range(n):
    x=int(input('Enter elements :'))
    list.append(x)
for p in permutation(list):
    print(p)