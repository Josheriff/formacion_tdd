
with description('Given numbers as string'):
    with description('returns the sum of the numbers separated by comma'):
        with it('empty string'):

            result = string_calculator(AN_EMPTY_STRING)
            expected_result = '0'
            expect(result).to(equal(expected_result))
