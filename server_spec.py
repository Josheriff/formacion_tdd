import requests


with description('Given an endpoint'):

    with it('If use get, returns all the agenda'):

        server_query =  requests.get('http://localhost:8080')
        print(server_query,'KAMEHAMEHAAAAAAAAAAAA')
        result = server_query.status

        expected_result = 200

        expect(result).to(equal(expected_result))


