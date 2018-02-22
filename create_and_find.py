# nombre, apellidos, tlf, correo, fecha creación
import json



def create_client(client):
    with open("data.json", "a") as myfile:
        myfile.write(client)
    return 201

def search_clients():
    with open('data.json', 'r') as myfile:
        data=myfile.read().replace('/n', ',')
        return data
###

from expects import expect, equal

CLIENT_BUSINESS_OBJECT = "{'name':'jose','surname':'Gallego','phone':'666666666','email':'fake@mail.com'}/n"
ANOTHER_CLIENT_BUSINESS_OBJECT = "{'name':'otroname','surname':'notanguapo','phone':'999999999','email':'morefake@mail.com'}/n"
CLIENT_CREATED = 201

with description('Create and search clients'):
    with description('Given the name, surname, tlf, email'):
        with it('we save all and add a timestamp'):

            result = create_client(CLIENT_BUSINESS_OBJECT)

            expected_result = CLIENT_CREATED

            expect(result).to(equal(expected_result))

            with open('data.json', 'w'): pass #after every test, the persistence must be cleaned

        with it('we can search the client'):

            create_client(CLIENT_BUSINESS_OBJECT)
            create_client(ANOTHER_CLIENT_BUSINESS_OBJECT)

            result = search_clients()
            preformated_result = CLIENT_BUSINESS_OBJECT + ANOTHER_CLIENT_BUSINESS_OBJECT
            expected_result = preformated_result.replace('/n',',')

            expect(result).to(equal(expected_result))

            with open('data.json', 'w'): pass #after every test, the persistence must be cleaned
