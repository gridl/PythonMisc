# start with  no defaults
def display_greeting(name,greeting='hello', times=2):
    times = max(1, times)
    for _ in range(0,times):
        print("{} {}".format(greeting,name))

display_greeting("jeff","good morning", 3)
display_greeting("michaal", 'gday', 1)

display_greeting("mark")
display_greeting("mark", "good afternoon")
display_greeting("mark", "good afternoon", 2)
display_greeting(name="michael",greeting="yo",times=4)
display_greeting("yo",times=4)
