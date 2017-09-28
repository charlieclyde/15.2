i = 1
what = []

while i <= 1000:
    what.append(i ** i)
    i = i + 1

print "%d" % (sum(what))
