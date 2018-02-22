###

def string_calculator(string):
    return '0'
###

from expects import expect, equal

AN_EMPTY_STRING = ''
NUMBER_WITH_NONE = '"","5"'

with description('Given numbers as string'):
    with description('returns the sum of the numbers separated by comma'):
        with it('given an empty string returns 0 in string format'):

            result = string_calculator(AN_EMPTY_STRING)
            expected_result = '0'
            expect(result).to(equal(expected_result))

        with description('given none and a number separated by commma'):
            with it('None equals to 0 and give the sum'):

                result = string_calculator(NUMBER_WITH_NONE)
                expected_result = '5'
                expect(result).to(equal(expected_result))


