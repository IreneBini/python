def square(x):
    """Function returning the suare of x.
    """
    return x**2.

# test function that test if the square function do what it has to do
def test():
    """Dumb unit test---make sure that the square of 3. is 9. using the square's function
    """
    assert square(3.) == 9.
    print('Passed---cool!')


if __name__ == '__main__':
    test()
