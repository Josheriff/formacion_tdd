# nombre, apellidos, tlf, correo, fecha creación

from expects import expect, equal

with description('Create and search clients'):
    with description('Given the name, surname, tlf, email'):
        with it('we save all and add a timestamp'):

            result = create_client(CLIENT_BUSINESS_OBJECT)

            expected_result = CLIENT_CREATED

            expect(result).to(equal(expected_result))

