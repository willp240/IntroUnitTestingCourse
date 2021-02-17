import numpy as np
import numpy.testing as npt
import pytest

from inflammation.models import daily_mean


def test_everything_works():
    npt.assert_array_equal(np.array([0, 0]), np.array([0, 0]))

def test_daily_mean_integers():
   """Test that mean function works for an array of positive integers."""
   from inflammation.models import daily_mean
   test_array = np.array([[1, 2],
                          [3, 4],
                          [5, 6]])
   # Need to use Numpy testing functions to compare arrays
   npt.assert_array_equal(np.array([3, 4]), daily_mean(test_array))

def test_daily_min_integers():
   """Test that min function works for an array of positive integers."""
   from inflammation.models import daily_min
   test_array = np.array([[1, 2],
                          [3, 4],
                          [5, 6]])
   # Need to use Numpy testing functions to compare arrays
   npt.assert_array_equal(np.array([1, 2]), daily_min(test_array))

def test_daily_max_integers():
   """Test that max function works for an array of positive integers."""
   from inflammation.models import daily_max
   test_array = np.array([[1, 2],
                          [3, 4],
                          [5, 6]])
   # Need to use Numpy testing functions to compare arrays
   npt.assert_array_equal(np.array([5, 6]), daily_max(test_array))

def test_daily_min_string():
   """Test for TypeError when passing strings"""
   from inflammation.models import daily_min
   from pytest import raises

   with raises(TypeError):
       daily_min([['Cannot', 'min'], ['string', 'arguments']])

@pytest.mark.parametrize(
   "test, expected",
   [
       ([[0, 0], [0, 0], [0, 0]], [0, 0]),
       ([[1, 2], [3, 4], [5, 6]], [3, 4]),
   ])
def test_daily_mean(test, expected):
    """Test mean function works for array of zeroes and positive integers.""" 
    from inflammation.models import daily_mean 
    npt.assert_array_equal(np.array(expected), daily_mean(np.array(test)))

@pytest.mark.parametrize(
   "test, expected",
   [
       ([[0, 0], [0, 0], [0, 0]], [0, 0]),
       ([[1, 2], [3, 4], [5, 6]], [1, 2]),
   ])
def test_daily_min(test, expected):
    """Test minn function works for array of zeroes and positive integers."""
    from inflammation.models import daily_min
    npt.assert_array_equal(np.array(expected), daily_min(np.array(test)))

@pytest.mark.parametrize(
   "test, expected",
   [
       ([[0, 0], [0, 0], [0, 0]], [0, 0]),
       ([[1, 2], [3, 4], [5, 6]], [5, 6]),
   ])
def test_daily_max(test, expected):
    """Test minn function works for array of zeroes and positive integers."""
    from inflammation.models import daily_max
    npt.assert_array_equal(np.array(expected), daily_max(np.array(test)))
