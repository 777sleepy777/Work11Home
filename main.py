from collections import UserDict
from datetime import datetime, date, time, timedelta
MAX_VALUE = 4
def input_error(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except KeyError:
            return "KeyError. This name is not in phone-book"
        except ValueError:
            return "ValueError. Phone number must be from 10 digit"
        except TypeError:
            return "TypeError. Unknown command"
        except IndexError:
            return "IndexError. Give me name and phone please"
    return inner

class Iterable:
    #MAX_VALUE = 4
    def __init__(self):
        self.current_value = 0

    def __next__(self):
        if self.current_value < MAX_VALUE:
            self.current_value += 1
            return self.current_value
        raise StopIteration
 
class CustomIterator():
    def __iter__(self):
        return Iterable()
       
class Field: 
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    
class Name(Field):
    def __setitem__(self, key, value):
        if value > 0:
            self.data.append(value)

    def __getitem__(self, idx=None):
        if idx is None:
            return self.data
        return self.data[idx]

class Birthday(Field):
    def __init__(self, value):
        self.value = Birthday.correct_birthday(value)
        
    def correct_birthday(date):
        if date:
            try:
                d = datetime.strptime(date, '%d %B %Y').date()
                return d
            except:
                    try:
                        d = datetime.strptime(date, '%d %b %Y').date()
                        return d 
                    except:
                        print('Invalid birthday date. Format "day" "month" "year"') 
                        return None   

    def __getitem__(self, idx=None):
        if idx is None:
            return self.data
        return self.data[idx]

    def __setitem__(self, date):
        self.value = Birthday.correct_birthday(date)

class Phone(Field):

    def __init__(self, value):
        self.value = value
  
    def __str__(self):
        return f"{self.value}"
    
    def __setitem__(self, value):

        if len(value) != 10 or not value.isdigit():
            raise ValueError("Number is not valid")
        else:
            self.value = value
    
    def __getitem__(self, idx=None):
        if idx is None:
            return self.data
        return self.data[idx]
 
class Record():

    def __init__(self, name, phone = None, birthday = None):
        self.name = Name(value=name)
        self.phones = []
        if phone:
            self.add_phone_number(value = phone)
        if birthday:
            self.birthday = Birthday(value=birthday)

        def __repr__(self):
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
   
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def days_to_birthday(self):
        
        if self.birthday.value != None:
            today = datetime.now().date()
            b_day = datetime(year=today.year, month=self.birthday.value.month, day=self.birthday.value.day).date()
            
            if b_day < today:
                b_day = datetime(year=today.year+1, month=self.birthday.value.month, day=self.birthday.value.day).date()
            time_diff = b_day - today
            tdays = time_diff.days
            if tdays == 0:
                print(f"Your birthday is today.")
            else:
                print(f"Your birthday is in {tdays} days.")

    def edit_phone(self, phone_old, phone_new):
        num = None
        for i in self.phones:
            if i.value == phone_old:
                num = phone_old
                i.value = phone_new

        if num is None:
        #    raise ValueError
        #if phone_old in self.phones:
        #   phone_old.value = phone_new 
        #else:
            raise ValueError



    def remove_phone(self, phone):
         for i in self.phones:
            if i.value == phone:
                self.phones.remove(i)

    def find_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                return i
   
        
class AddressBook(UserDict):
    
    def add_record(self, record: Record):
        self.data[record.name.value] = record
    
    def find(self, name: Name):
         for i in self.data:
            if i == name:
                return self.data[i]
    
    def iterator(self):
        c = CustomIterator()
        #for key, value in self.items():
        for i in c:
            print(self)
            print("------------------------")

   
    def delete(self, name: Name):
        try:
            self.data.pop(name)
        except:
            KeyError       

def main():
  
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John", "", '30 May 2020')
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    #john_record.days_to_birthday()

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    #for name, record in book.data.items():
    #    print(name, record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    #found_phone = john.find_phone("5555555555")
    #print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    #book.delete("Jane")
    jane_record2 = Record("Jane2")
    jane_record2.add_phone("9876543210")
    book.add_record(jane_record2)
    jane_record3 = Record("Jane3")
    jane_record3.add_phone("9876543210")
    book.add_record(jane_record3)
    jane_record4 = Record("Jane4")
    jane_record4.add_phone("9876543210")
    book.add_record(jane_record4)
    jane_record5 = Record("Jane5")
    jane_record5.add_phone("9876543210")
    book.add_record(jane_record5)
    jane_record6 = Record("Jane6")
    jane_record6.add_phone("9876543210")
    book.add_record(jane_record6)
    book.iterator()

    
if __name__ == '__main__':
    main()