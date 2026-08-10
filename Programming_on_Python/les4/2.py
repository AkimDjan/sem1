from dataclasses import dataclass, asdict
from string import ascii_lowercase, ascii_uppercase, digits
from uuid import (
    UUID,
    uuid4,
)

@dataclass
class Person:
    login: str
    password: str
    username: str
    metadata: str = ""


class PersonDB:
    _database: dict[UUID, Person]
    _login_registry: set[str]
    check=set(ascii_lowercase+ascii_uppercase+digits)

    def __init__(self, _database={}, _login_registry=set()) -> None:
        self._database={}
        self._login_registry=set()
    
    def _good_login(self, person: Person) -> bool:
        for i in person.login:
            if i not in self.check:
                return False
        if (person.login in self._login_registry) or person.login=='':
            return False
        return True
    
    def _good_password(self, person: Person) -> bool:
        good_len=10
        upp_c, low_c, digit_=0,0,0
        for i in person.password:
            if i not in self.check:
                return False
            if i in ascii_lowercase:
                low_c=1
            elif i in ascii_uppercase:
                upp_c=1
            elif i in digits:
                digit_=1
            else: 
                return False
        if upp_c+low_c+digit_!=3:
            return False
        if len(person.password)<good_len:
            return False
        return True


    def create_person(self, person: Person) -> UUID:
        
        if self._good_login(person) and self._good_password(person):
            uniq_id=uuid4()
            self._login_registry|={person.login}
            self._database[uniq_id]=person
            return uniq_id
        else:
            raise ValueError
    
    def read_person_info(self, person_id: UUID) -> Person:
        if person_id not in self._database:
            raise KeyError
        return self._database[person_id]
    
    
    def update_person_info(self, person_id: UUID, person_info_new: Person) -> None:

        if person_id not in self._database:
            raise KeyError
        if person_info_new.login != '' and self._good_login(person):
            self._login_registry.remove(self._database[person_id].login)
            self._database[person_id].login=person_info_new.login
            self._login_registry|={person_info_new.login}
        
        
        if person_info_new.password != '' and self._good_password(person):
            self._database[person_id].password=person_info_new.password
        
        if person_info_new.username!='':
            self._database[person_id].username=person_info_new.username
        
        if person_info_new.metadata!='':
            self._database[person_id].metadata=person_info_new.metadata

        

    def delete_person(self, person_id: UUID) -> None:
        if person_id not in self._database:
            raise KeyError
        self._login_registry.remove(self._database[person_id].login)
        self._database.pop(person_id)
        

#--------------------------------------------------


person1 = Person(
    password="Aa1Bb2Cc3Dd4",
    login="login1",
    username="user#1",
)

database = PersonDB()
person1_id = database.create_person(person1)


assert len(database._database) == 1
assert len(database._login_registry) == 1
assert person1_id in database._database
assert person1.login in database._login_registry
assert database._database[person1_id] == person1




persons_wrong = {
    "no-login": Person(
        password="Aa1Bb2Cc3Dd4",
        login="",
        username="user#2",
    ),
    "existed-login": Person(
        password="Aa1Bb2Cc3Dd4",
        login="login1",
        username="user#2",
    ),
    "too-short-password": Person(
        password="12345",
        login="login2",
        username="user#2",
    ),
    "no-lower": Person(
        password="A1B2C3D4E5F",
        login="login2",
        username="user#2",
    ),
    "no-upper": Person(
        password="a1b2c3d4e5f",
        login="login2",
        username="user#2",
    ),
    "no-digits": Person(
        password="aAbBcCdDeEf",
        login="login2",
        username="user#2",
    ),
}

for test_name, wrong_person in persons_wrong.items():
    try:
        database.create_person(wrong_person)
        assert False, test_name

    except ValueError:
        assert True
        assert len(database._database) == 1
        assert len(database._login_registry) == 1
#ПРОШЛО
#-----------------------------------------------------------


person = database.read_person_info(person1_id)
assert person1 == person
assert len(database._database) == 1
assert len(database._login_registry) == 1

try:
    fake_id = uuid4()
    person = database.read_person_info(fake_id)
    assert False

except KeyError:
    assert True
    assert len(database._database) == 1
    assert len(database._login_registry) == 1
#ПРОШЛО
#-----------------------------------------------------


person2 = Person(
    password="AaBbcC1234Dd",
    login="login2",
    username="user#2"
)

'''person2_copy= Person(
    password="AaBbcC1234Dd",
    login="login2",
    username="user#2"
)'''

person2_id = database.create_person(person2)
assert len(database._database) == 2
assert len(database._login_registry) == 2
assert person2_id in database._database
assert person2.login in database._login_registry
assert database._database[person2_id] == person2

person2_updated = Person(
    password="abcDEF123456",
    login="LOGIN2",
    username="user#2",
)
person2_update = Person(
    password="abcDEF123456",
    login="LOGIN2",
    username="",
)

database.update_person_info(person2_id, person2_update)
assert len(database._database) == 2
assert len(database._login_registry) == 2
assert person2_id in database._database
assert person2.login not in database._login_registry
assert person2_updated.login in database._login_registry
assert database._database[person2_id] == person2_updated

#ПРОШЛО
#----------------------------------------------------


try:
    fake_id = uuid4()
    database.delete_person(fake_id)
    assert False

except KeyError:
    assert True
    assert len(database._database) == 2
    assert len(database._login_registry) == 2

database.delete_person(person2_id)
assert len(database._database) == 1
assert len(database._login_registry) == 1
assert person2_id not in database._database
assert person2_updated.login not in database._login_registry

#---------------------------------------------