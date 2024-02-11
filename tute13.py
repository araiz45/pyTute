# for loop 
staff = [["cpu", "mouse", "screen", "keyboard"], ["pencil", "board", "calculator", "book"], ["varniar caliper", "screw gauage", "book"]]
 
for things in staff:
    print(things)
    for thing in things:
        print(thing)
        for letter in thing:
            print(letter)
            if(letter == "p"):
                break