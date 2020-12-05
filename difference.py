list1 = ["r", "n", "b", "q", "k", "b", "n", "r",
        "p", "p", "p", "p", "p", "p", "p", "p",
        ".", ".", ".", ".", ".", ".", ".", ".",
        ".", ".", ".", ".", ".", ".", ".", ".",
        ".", ".", ".", ".", ".", ".", ".", ".",
        ".", ".", ".", ".", ".", ".", ".", ".",
        "P", "P", "P", "P", "P", "P", "P", "P",
        "R", "N", "B", "Q", "K", "B", "N", "R"]

list2 = ["r", "n", "b", "q", "k", "b", ".", "r",
        "p", ".", "p", "p", "p", "p", "p", "p",
        ".", ".", ".", ".", ".", ".", ".", ".",
        ".", "p", ".", ".", ".", ".", ".", ".",
        ".", ".", ".", ".", ".", ".", ".", ".",
        ".", ".", ".", ".", ".", "P", ".", ".",
        "P", "P", "P", "P", "P", ".", "P", "P",
        ".", "N", "B", "Q", "K", "B", "N", "R"]

def find_difference(list1: list, list2: list) -> list:
    """
    A function that finds the differences in two lists and returns a list of where the values are different.\n

    Takes in 2 lists which must be the same length.
    It then finds the differences in the list and returns them as an another list.
    """

    differences = []

    for i in range(len(list1)):
        val1 = list1[i]
        val2 = list2[i]

        if val1 != val2:
            differences.append(i)
    
    return differences

dif = find_difference(list1, list2)
print(dif)