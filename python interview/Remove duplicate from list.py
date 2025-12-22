# "one","two","three","one","two"
def remove_duplicate(l):
    out = []
    for i in l:
        if i not in out:
            out.append(i)
    return out
l = ["one","two","three","one","two"]
result = remove_duplicate(l)
print(result)
