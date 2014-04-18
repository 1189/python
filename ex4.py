cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."




pencils = 2
erasers = 4
pens = 3
rulers = erasers + pens - 4
highlighters = 6
crayons = pencils * highlighters
protractors = highlighters - rulers
sharpeners = (pens + rulers) / protractors

print "I have", pencils, "pencils."
print "I have", erasers, "erasers, how many more erasers do I have than pencils?"
print erasers - pencils
print "I have", pens - 1, "pens, but I'm going to buy one more later. I will have", pens, "pens."
print "I have", rulers, "rulers and", highlighters, "highlighters."
print "Tim has", crayons - 2, "crayons. I have 2 more than him. I have", crayons, "crayons."
print "I have", protractors, "protractors."
print "I also have", sharpeners, "sharpeners. My brother has", sharpeners * 2, "sharpeners."
