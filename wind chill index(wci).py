v=int(input("enter the wind speed"))
t=int(input("enter the temperature"))
if 0<=v<=4:
    wci=t
    print(wci)
elif v>=45:
    wci=1.6*t-55
    print(wci)
else:
    wci=91.4+(91.4-t)*(0.0203*v-0.304*v*0.5-0.474)
    print(wci)