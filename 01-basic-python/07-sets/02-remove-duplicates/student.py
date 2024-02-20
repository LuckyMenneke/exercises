# Write your code here
def remove_duplicates(ns):
    found = set()
    result = []
    for x in ns:
        if x not in found:
            found.add(x)
            result.append(x)
    return result

