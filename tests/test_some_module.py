from src.job.some_module import convert_to_int

class TestConvertToInt:

    def test_convert_to_int(self):

        test_values = ['756',756.0,]

        for value in test_values:
            assert value == 756,'Value should be 756 but got {}'.format(value)