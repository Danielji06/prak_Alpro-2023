inch = int(input("Masukkan jarak dalam inch: "))
feet = 12
yard = 3 * feet
mile = 1760 * yard


hasil_mile = inch // mile
hasil_yard = (inch - hasil_mile * mile)// yard
hasil_feet = (inch - hasil_mile * mile - hasil_yard * yard)// feet
hasil_inch = (inch - hasil_mile * mile - hasil_yard * yard - hasil_feet * feet)

print(f"{inch} inch = {hasil_mile} mile {hasil_yard} yard {hasil_feet} feet {hasil_inch} inch")