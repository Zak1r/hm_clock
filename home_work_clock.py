
# clock value
hours = int (input('Enter hours: '))
mins = int (input('Enter mins: '))
delta = int (input('Enter delta: '))
if hours >= 0 and mins >= 0:
    new_hours = (hours + delta) % 24
if new_hours <= 9: new_hours = '0' + str (new_hours)
if mins <= 9: mins = '0' + str (mins)
print(f'{new_hours}:{mins}')