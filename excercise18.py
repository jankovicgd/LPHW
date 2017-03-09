def print_two(*args):
    arg1, arg2 = args
    print "arg1 %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
    print "arg1: %r" % arg1

print_two("Nikola", "Jankovic")
print_one("je_kralj")
