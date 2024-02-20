# Write your code here
def target_sum(ns, target):
    for x in range(len(ns)):
        for y in range(len(ns)):
            if x != y and ns[x] + ns[y] == target:
                return True
    return False
