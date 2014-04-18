my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
    
    
    
    
name = 'Eric'
age = 15
height = 173.0 # cm
weight = 64.0 # kg
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print "My name is %s." % name
print "I am %d years old." % age
print "I am %d cm tall, which is around %d inches." % (height, height * 0.393701)
print "I am %d kg heavy, which is about %d pounds." % (weight, weight * 2.20462)
print "I have %s eyes, %s teeth and %s hair." % (eyes, teeth, hair)

a = 7.0
b = 18.0
c = 141.0
d = 59.0
e = 76.0
f = 12.0
g = 4.5
h = 6.9

print "What is 7 + 59?"
print "%s" % (a + d)
print "If I add 7 and 76, I get %s. If I divide that by 18, I get %s." % (a + e, (a + e) / b)
print "If I subtract %s from %s, I get %s." % (h, f, f - h)
