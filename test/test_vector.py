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
    vector.pushback(0)
    vector.pushback(4)
    vector.pushback(7)
    return vector

class TestVector:
    def test_getCapacity(self, vector_with_elements: Vector) -> None:
        assert vector_with_elements.getCapacity() == 3
        
    def test_getSize(self, vector_with_elements: Vector) -> None:
        assert vector_with_elements.getSize() == 3
        
    def test_popback(self, vector_with_elements: Vector) -> None:
        assert vector_with_elements.popback() == 7
    
    def test_set(self, vector_with_elements: Vector) -> None:
        assert vector_with_elements.array == [0, 4, 7]
        
    def test_get(self, vector_with_elements: Vector) -> None:
        assert vector_with_elements.get(0) == 0
        assert vector_with_elements.get(1) == 4
        assert vector_with_elements.get(2) == 7

    def test_resize(self, vector_with_elements: Vector) -> None:
        initial_capacity = vector_with_elements.getCapacity()
        
        vector_with_elements.resize()
        
        assert vector_with_elements.getCapacity() == 2 * initial_capacity

    def test_pushback_when_array_empty(self, vector: Vector) -> None:
        vector.pushback(0)
        
        assert vector.get(0) == 0
        assert vector.getSize() == 1
        assert vector.getCapacity() == 3

    def test_pushback_when_array_full(self, vector_with_elements: Vector) -> None:
        initial_capacity = vector_with_elements.getCapacity()
        
        vector_with_elements.pushback(9)
        
        assert vector_with_elements.get(0) == 0
        assert vector_with_elements.get(1) == 4
        assert vector_with_elements.get(2) == 7
        assert vector_with_elements.get(3) == 9
        assert vector_with_elements.getSize() == 4
        assert vector_with_elements.getCapacity() == 2 * initial_capacity
    
    def test_capacity_no_resize(self) -> None:
        vector = Vector(1)
        
        assert vector.getSize() == 0
        assert vector.getCapacity() == 1
        
    def test_capacity_resize_grow(self) -> None:
        vector = Vector(1)
        vector.pushback(1)
        
        assert vector.getCapacity() == 1
        
        vector.pushback(2)
        assert vector.getCapacity() == 2
        
    def test_capacity_resize_shrink(self) -> None:
        vector = Vector(1)
        
        assert vector.getSize() == 0
        assert vector.getCapacity() == 1
        
        vector.pushback(1)
        
        assert vector.getSize() == 1
        assert vector.getCapacity() == 1
        
        vector.pushback(2)
        
        assert vector.getSize() == 2
        assert vector.getCapacity() == 2
        
        assert vector.get(1) == 2
        
        vector.set(1, 3)
        
        assert vector.get(1) == 3
        assert vector.popback() == 3
        assert vector.getSize() == 1
        assert vector.getCapacity() == 2
        