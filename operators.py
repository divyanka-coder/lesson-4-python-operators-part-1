field1=240
field2=160
field3=310
field4=124
field5=244
field6=99
total=field1+field2+field3+field4+field5+field6
average=total/6
print("total harvest=",total,"kg")
print("average for per field=",average,"kg")

price_per_kg=20
earnings=total*price_per_kg
print("total earnings :rs.",earnings)

bags=total//30
leftover= total%30
print("full bags packed:",bags)
print("leftover grains:",leftover,"kg")

lastyear=500
print("better than last year?",total>lastyear)
print("same as last year?",total==lastyear)
print("not better than last year?",total<lastyear)

total+=30
print("after bonus crop:",total,"kg")

total-=15
print("after seed reserve:",total,"kg")

bags=total//30
print("final bags packed :",bags)