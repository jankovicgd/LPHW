from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that hit CTRL-C"
print "If you do want that, hit Return."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now add three lines."
line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm writing this to the file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print "And we close it."

target.close()
