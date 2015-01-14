

def simple_unittest_function(test_name, left_value, right_value):
    """

    """
    try:
        assert left_value == right_value
        print("Test Passed: {}".format(test_name))
    except AssertionError:
        print("Test Failed: {}".format(test_name))

    return
