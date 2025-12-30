import pytest
from src.scwb_calculator import SCWBCalculator

def test_strong_column_weak_beam():
    """Test a case where the column is strong enough."""
    calculator = SCWBCalculator(factor=1.2)
    # Sum Mc = 100, Sum Mb = 50. Required Mc = 1.2 * 50 = 60. 100 >= 60. Safe.
    result = calculator.check_joint(sum_mc=100, sum_mb=50)
    assert result['is_safe'] is True
    assert result['message'] == "Strong Column Weak Beam Satisfied"

def test_weak_column():
    """Test a case where the column is too weak."""
    calculator = SCWBCalculator(factor=1.2)
    # Sum Mc = 60, Sum Mb = 60. Required Mc = 1.2 * 60 = 72. 60 < 72. Unsafe.
    result = calculator.check_joint(sum_mc=60, sum_mb=60)
    assert result['is_safe'] is False
    assert result['message'] == "WARNING: Weak Column Detected"

def test_zero_beam_moment():
    """Test edge case with zero beam moment."""
    calculator = SCWBCalculator(factor=1.2)
    result = calculator.check_joint(sum_mc=100, sum_mb=0)
    assert result['is_safe'] is True
    assert result['ratio'] == float('inf')
