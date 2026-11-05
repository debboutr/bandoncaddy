import sqlite3
from datetime import datetime
from random import shuffle

try:
    # 1. Connect to the database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # 2. Execute SELECT query
    cursor.execute("SELECT * FROM people")

    # 3. Fetch and print all records
    rows = cursor.fetchall()
    rick = User.objects.first()
    check = 0

    for row in rows:
        print(row)
        pk, first, last, notes, lat, lon, group, img = row
        if group != check:
            party = Party.objects.create(pk=group, name=f"{first}-{last}".upper(), author=rick)
            check = group

        Person.objects.create(
                pk=pk,
                first_name=first,
                last_name=last if last else '',
                notes=notes if notes else '',
                lat=lat if lat else '',
                lon=lon if lon else '',
                group=party,
                image=img)

    tracks = list(Course.objects.all())

    cursor.execute("SELECT * FROM loops")
    rows = cursor.fetchall()
    tot = []
    for row in rows:
        if row[0] == 536 or row[0] == 13:
            continue
        _, date, wage, bags, _, group, courses = row
        dt = datetime.strptime(date, '%Y-%m-%d')   
        party = Party.objects.get(pk=group)

        if courses == None:
            if bags > 2:
                wage = wage / 2
                shuffle(tracks)
                course = tracks[0]
                Loop.objects.create(wage=wage, bags=2, date=dt, group=party, course=course, author=rick)
                shuffle(tracks)
                course = tracks[0]
                Loop.objects.create(wage=wage, bags=bags-2, date=dt, group=party, course=course, author=rick)
            else:
                shuffle(tracks)
                course = tracks[0]
                Loop.objects.create(wage=wage, bags=bags, date=dt, group=party, course=course, author=rick)
        elif ',' in courses:
            one, two = courses.split(',')
            if one == 'pac':
                one = 'pacific'
            if two == 'pac':
                two = 'pacific'
            Loop.objects.create(wage=wage / 2, bags=2, date=dt, group=party, course=Course.objects.get(name=one), author=rick)
            Loop.objects.create(wage=wage / 2, bags=bags-2, date=dt, group=party, course=Course.objects.get(name=two), author=rick)
        else:
            if courses == 'pac':
                courses = 'pacific'
            course = Course.objects.get(name=courses)
            Loop.objects.create(wage=wage, bags=bags, date=dt, group=party, course=course, author=rick)
        print(row)

except sqlite3.Error as e:
    print(f"Error: {e}")
finally:
    if conn:
        conn.close()   
