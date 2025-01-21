import pytest

class Calculator:
    def add(self, a, b):
        return a + b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Não é possível dividir por zero")
        return a / b

def test_calculator_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0

def test_calculator_divide():
    calc = Calculator()
    assert calc.divide(6, 2) == 3
    assert calc.divide(5, 2) == 2.5
    
    with pytest.raises(ValueError):
        calc.divide(10, 0)

if __name__ == '__main__':
    pytest.main([__file__])
