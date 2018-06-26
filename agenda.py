# -*- coding: utf-8 -*-

'''
    Agenda telefónica básica.

'''
import csv
class Contact:
    def __init__(self, contactData):
        self.data = contactData

class Agenda:
    def __init__(self):
        self.contacts = []
        self._fileName = 'contacts.csv'

    def addContact(self, contactData):
        self.contacts.append(contactData)
        self._save()

    def searchContact(self, criteria):
        if len(self.contacts) > 0:
            for ix, ct in enumerate(self.contacts):
                if criteria in str(ct).lower():
                    print (ix, ct)
                    return ix
                else:   
                    print ("No encontrado")
        else:
            print ("La agenda está vacía")

    def delete(self, criteria):
        index = self.searchContact(criteria=criteria)
        del self.contacts[index]
        print (self.contacts)
        self._save()

    def updateContact(self, criteria):
        index = self.searchContact(criteria=criteria)
        contactData = {}
        contactData['nombre'] = input("Ingrese el nuevo nombre del contacto")
        contactData['telefono'] = input("Ingrese el nuevo teléfono del contacto")
        contactData['email'] = input("Ingrese el nuevo email del contacto")

        self.contacts[index] = contactData
        self._save()

    def _save(self):
        with open(self._fileName, 'w') as f:
            writer = csv.DictWriter(f, fieldnames = self.contacts[0].keys())
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow(contact)


    def __str__(self):
        return str(self.contacts)

def run():
    contact_book = Agenda()
    while True:
        command = input(
            '''¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''
        )
        if command == 'a':
            contactData = {}
            contactData['nombre'] = input("Ingrese nombre del contacto")
            contactData['telefono'] = input("Ingrese teléfono del contacto")
            contactData['email'] = input("Ingrese email del contacto")
            contact = Contact(contactData)
            contact_book.addContact(contactData=contact.data)

        elif command == 'ac':
            print('actualizar contacto')
            criteria = input("Ingresa una palabra clave: ")
            contact_book.updateContact(criteria)

        elif command == 'b':
            print('buscar contacto')
            criteria = input("Ingresa una palabra clave: ")
            contact_book.searchContact(criteria=criteria)

        elif command == 'e':
            print('eliminar contacto')
            criteria = input("Ingresa una palabra clave: ")
            contact_book.delete(criteria=criteria)
            

        elif command == 'l':
            print('listar contactos')
            print (contact_book)

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')
    pass

if __name__ == "__main__":
    print ("Bienvenido")
    run()