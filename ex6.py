x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e




a = "There are %d animals." % (9 + 11 + 14 + 4 + 6)
b = "There are %d dogs." % 9
c = "There are %d cats." % 11
d = "There are %d hamsters." % 14
e = "There are %d turtles." % 4
f = "There are %d snails." % 6

print a
print b
print c
print d
print e
print f

g = 'Tim'
h = 'Jake'
i = True

j = "Is %s taller than %s? %s"
print j % (g, h, i)
