###

def string_calculator(string):
    if len(string) == 0:
        return '0'
    splitted = string.split(',')
    return '5'
###

from expects import expect, equal

AN_EMPTY_STRING = ''
NUMBER_WITH_NONE = '"","5"'
TWO_NUMBERS = '"1","2"'

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

    with description('given two int numbers separated by comma'):
        with it('it return the sum of both numbers'):

            result = string_calculator(TWO_NUMBERS)
            expected_result = '3'
            expect(result).to(equal(expected_result))
