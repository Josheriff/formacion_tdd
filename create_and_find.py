# nombre, apellidos, tlf, correo, fecha creación
import json



def create_client(client):
    with open("data.json", "a") as myfile:
        myfile.write(client)
    return 201

###

from expects import expect, equal

CLIENT_BUSINESS_OBJECT = "{'name':'jose','surname':'Gallego','phone':'666666666','email':'fake@mail.com'}"
CLIENT_CREATED = 201

with description('Create and search clients'):
    with description('Given the name, surname, tlf, email'):
        with it('we save all and add a timestamp'):

            result = create_client(CLIENT_BUSINESS_OBJECT)

            expected_result = CLIENT_CREATED

            expect(result).to(equal(expected_result))

            with open('data.json', 'w'): pass
