from experiment import Experiment
from pytest import approx


def test_probability_of_a_head():
    e = Experiment()
    p = e.flip_coin_x_times(100_000)
    assert p == approx(0.5, rel=0.01)


def test_probability_of_hh():
    e = Experiment()
    p = e.flip_coin_2x_n_times(100_000)
    assert p == approx(0.25, rel=0.01)


def test_probability_of_ththh():
    e = Experiment()
    p = e.flip_coin_with_pattern_n_times([0, 1, 0, 1, 1], 1_000_000, 5)
    assert p == approx((0.5)**5, rel=0.01)
