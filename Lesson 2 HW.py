Math=input ('math score?')
eng=input ('english score?')
eng=int(eng)
Math=int(Math)
if eng >= 90 and Math >= 90:
    print("have gift")
    
if eng < 90 and Math < 90:
    print("Punishment")
    
elif eng < 90 and Math > 90:
    print('try more')