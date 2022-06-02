import time
##99Bottles of beer song

bottlesofbeer = 99
while bottlesofbeer > 0:
    print(bottlesofbeer,"Bottles of beer on the wall")
    print(bottlesofbeer,"Bottles of beer")
    print("Take one down, pass it around")
    bottlesofbeer = bottlesofbeer - 1
    print(bottlesofbeer,"Bottles of beer on the wall")
    time.sleep(1)