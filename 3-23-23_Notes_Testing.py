import pytest

class Fruit:
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return self.name == other.name


@pytest.fixture
def my_fruit():
    print("Creating apple")
    return Fruit('apple')


@pytest.fixture
def fruit_basket(my_fruit):
    print("Arrange: Creating basket")
    basket = [Fruit("banana"), my_fruit]
    yield [Fruit("banana"), my_fruit]
    print("Cleanup")
    basket.clear()


def test_basket(fruit_basket):
    assert my_fruit() in fruit_basket()

# things fucked
