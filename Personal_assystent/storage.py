from error_handlers import input_error
from Address_book.address_book import AddressBook
from Address_book.record import Record
from Address_book.fields import Phone

contacts = AddressBook()

@input_error
def add_contact(name, phone):
    """
    Додає новий контакт.
    """
    record = Record(name)
    record.add_phone(phone)
    contacts.add_record(record)
    return f"Contact '{name}' added with phone '{phone}'."

@input_error
def change_contact(name, new_phone):
    """
    Змінює існуючий контакт.
    """
    record = contacts.find(name)
    if not record:
        return f"Contact '{name}' not found."
    if not record.phones:
        return f"Contact '{name}' has no phone numbers to change."
    
    old_phone = record.phones[0].value
    record.edit_phone(old_phone, new_phone)
    return f"Contact '{name}' updated: '{old_phone}' → '{new_phone}'."


@input_error
def show_phone(name):
    """
    Виводить номер телефону для вказаного імені.
    """
    record = contacts.find(name)
    if record:
        return str(record)
    return f"Contact '{name}' not found."

@input_error
def show_all():
    """
    Виводить усі контакти та номери телефонів.
    """
    if not contacts.data:
        return "No contacts found."
    return str(contacts)