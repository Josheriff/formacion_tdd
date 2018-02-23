import requests


with description('Given the name, surname, tlf, email'):

    with it('we save all and add a timestamp'):

        result =  requests.get('https://localhost:8080').status

        expected_result = 200

        expect(result).to(equal(expected_result))


