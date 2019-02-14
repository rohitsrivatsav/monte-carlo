from experiment import Experiment
from pytest import approx


def test_probability_of_a_head():
    e = Experiment()
    p = e.flip_coin_x_times(100_000)
    assert p == approx(0.5, rel=0.01)
