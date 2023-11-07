from my_math_lib import SimpleMathLib

simple_math_lib = SimpleMathLib()

def test_add():

    expected = 6
    actual = simple_math_lib.add(1,2,3)

    assert expected == actual

def test_add_list():

    nums = [2, 3, 4, 5]

    expected = sum(nums)
    actual = simple_math_lib.add(*nums)

    assert  expected == actual
    
def test_multiply():
    m = SimpleMathLib
    expected = 12
    actual = m.multiply(2, 3, 4)
    assert expected == actual

def test_multiply_list():
    
    nums = [2, 3, 4]
    expected = 12
    actual = SimpleMathLib.multiply(*nums)

    assert expected == actual