class User:

    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        print('User created')

    def introduce_yourself(self, guest_name):
        print(f"Hi {guest_name}, I am {self.name}, contact me at {self.email}")

    # __repr__() gibt eine technische Darstellung des Objekts zurück – nützlich für Debugging.

    def __repr__(self):
        return f"User(username = '{self.username}', name = '{self.name}', email = '{self.email}')"

# __str__() wird verwendet, wenn du print(user) aufrufst.
# hier gibt __str()__ das ergebnis von __repr()__ zurück

    def __str__(self):
        return self.__repr__()


# Erstellt ein neues Objekt user2
# Ausgabe: User created
user2 = User("john", "John Doe", "john@doe.com")
# Ausgabe: Hi David, I am John Doe, contact me at john@doe.com
user2.introduce_yourself("David")
print(1111111111)
user3 = User("jane", "Jane Doe", "jane@doe.com")
user3.introduce_yourself("David")
print(22222222)
user4 = User('jane', 'Jane Doe', 'jane@doe.com')
# print(user4) ruft __str__() auf → das wiederum ruft __repr__() auf → Ausgabe:
print(user4)
print(1111111)
class UserDatabase:
    # Konstruktor: initialisiert die Datenban mit einer leeren Liste namens users
    def __init__(self):
        self.users = []
    # Benutzer einfügen sortiert nach username
    # fügt neuen Benmutzer alphabetisch sortiert nach username ein in Liste
    # wenn zb user.username = "bernd", dann zwischen "armin" und "colin"

    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)
    # Durchsucht die Liste nach einem Benutzer mit dem passenden username
    # Gibt das User -Objekt zurück, wenn gefunden
    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
    # Benutzer aktualisieren
    # Sucht Benutzer mit user.username und aktualisiert dessen name und email

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    # Alle Benutzer zurückgeben
    # Gibt die gesamte Benutzerliste zurück
    def list_all(self):
        return self.users

# Beispielobjekte, erstelle vier User -Objekte
armin = User('armin', 'Armin Aal', 'armin@web.de')
bernd = User('bernd', 'Bernd Brot', 'bernd@google.com')
colin = User('colin', 'Colin Col', 'colin@web.de')
david = User('david', 'david degen', 'david@google.com')

# Speichert sie in einer Liste - aber nicht in Datenbank UserDatabase.
# Muss noch mit insert() eingefügt werden.
users = [armin, bernd, colin, david]
# gibt Daten von bernd aus
print(bernd.username, bernd.email, bernd.name)
# vergleicht zwei Strings alphabetisch:
# "Abend" kommt vor "Bernd" -> Ergebnis: True
print("Abend" < "Bernd")



print('----------------------')
names = ['bernd', 'arndt', 'david', 'colin']
def sorted_list(users):
    liste = []
    # für jeden Namen wird eine Einfügeposition person_stelle gesucht.
    for person in users:
        person_stelle = 0
        # vergleicht person mit den bereits eingefügten Namen
        while person_stelle < len(liste):
            # solange person alphabetisch größer ist, wird person_stelle erhöht
            if person > liste[person_stelle]:
              person_stelle += 1
            # sobald ein größerer oder gleicher Name gefunden wird, wird Schleife abgebrochen
            else:
                break
        # führt eine gezielte Einfügung eines Elements (person) an einer bestimmten Position (person_stelle) in die Liste liste durch.
        liste.insert(person_stelle, person)

    return liste

print(sorted_list(names))


names = ['bernd', 'arndt', 'david', 'colin']
sorted_names = sorted(names)
print(sorted_names)

verdopple = lambda x: x * 2
print(verdopple(5))  # Ergebnis: 10
addiere = lambda a, b: a + b
print(addiere(3, 7))  # Ergebnis: 10
zahlen = [1, 2, 3, 4]
verdoppelt = list(map(lambda x: x * 2, zahlen))
print(verdoppelt)  # Ergebnis: [2, 4, 6, 8] lambda wird auf jedes element in liste zahlen angewendet
zahlen = [1, 2, 3, 4, 5, 6]
ungerade = list(filter(lambda x: x % 2 != 0, zahlen))
print(ungerade)  # Ergebnis: [1, 3, 5]

