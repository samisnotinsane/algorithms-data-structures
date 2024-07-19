import pytest
from datastructure.array import Vector

@pytest.fixture
def capacity() -> int:
    return 3

@pytest.fixture
def vector(capacity: int) -> Vector:
    return Vector(capacity)

@pytest.fixture
def vector_with_elements(vector: Vector) -> Vector:
    vector.set(0, 0)
    vector.set(1, 4)
    vector.set(2, 7)
    return vector

class TestVector:
    def test_set(self, vector_with_elements: Vector) -> None:
        assert vector_with_elements.array == [0, 4, 7]
        
    def test_get(self, vector_with_elements: Vector) -> None:
        assert vector_with_elements.get(0) == 0
        assert vector_with_elements.get(1) == 4
        assert vector_with_elements.get(2) == 7
        