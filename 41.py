hour = int(input("Enter hour (0-12): "))
minute = int(input("Enter minute (0-59): "))

hour = hour % 12
hour_angle = 0.5 * (hour * 60 + minute)
minute_angle = 6 * minute
angle = abs(hour_angle - minute_angle)
angle = min(angle, 360 - angle)
print(f"Angle between hands: {angle:.2f} degrees")
