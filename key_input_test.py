while True:
    try:
        c = raw_input("Change speed: ")
        if c == 'w' :
            print "Increasing speed"
        elif c == 's' :
            print "Decreasing speed"
    except KeyboardInterrupt: #Triggered by pressing Ctrl+C
        print "Bye"
        break #Exit