precipitation = True
temperature =+8

if precipitation:
    if temperature > 0:
        print ('Bring your umbrella')
    else:
        print ('Wear your boots and winter')

if precipitation and temperature > 0:
        print ('Bring your umbrella')
elif precipitation:        
        print ('Wear your boots and winter')
