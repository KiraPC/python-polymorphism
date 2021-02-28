import sys
import pytest
from pathlib import Path

main_dir = Path(__file__).parent.parent
sys.path.insert(0, str(main_dir))

from python_polymorphism import Poly
from python_polymorphism.lib.types import PolyMethodArgumentsException

polymorphic = Poly()
class PolyClass():
    @polymorphic.this()
    def test_poly_fn(self, my_first_test_argument):
        return 'my_first_test_argument'
    
    @polymorphic.this()
    def test_poly_fn(self, my_second_test_argument):
        return 'my_second_test_argument'
    
poly_class = PolyClass()

def test_with_correct_arg():
    response = poly_class.test_poly_fn(
        my_first_test_argument=1
    )
    assert response == 'my_first_test_argument'

    response = poly_class.test_poly_fn(
        my_second_test_argument=1
    ) 
    assert response == 'my_second_test_argument'

def test_with_uncorrect_arg():
    with pytest.raises(PolyMethodArgumentsException):
        poly_class.test_poly_fn(
            my_generic_test_argument=1
        )
