print "Lets practice everything"
print "Escape di\'s with \\ before \t woo im tabbed \n and im on a new line"

poem = """
O lepi svete
Ja sam dete
Volim cvete
trt
"""

print "------------------"
print poem
print "------------------"

five = 10 - 2 + 3 - 6
print five

def seceret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = seceret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We have %d beans, %d jars, and %d crates." % (beans, jars, crates)
