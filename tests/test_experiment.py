from experiment import Experiment
from pytest import approx


def test_probability_of_one_head():
    e = Experiment()
    p = e.flip_coin_x_times(100000)
    assert p == approx(0.5, rel=0.01)


def test_probability_of_HH():
    e = Experiment()
    p = e.flip_coin_2x_n_times(100_000)
    assert p == approx(0.25, rel=0.01)


# def test_biased_probability_of_HHHH():
#     e = Experiment()
#     p = e.flip_biased_coin_4x_n_times(100_00000)
#     assert p == approx(0.3**4, rel=0.01)


def test_probability_of_THTHH():
    e = Experiment()
    p = e.flip_coin_1t1h1t2h_n_times(100_0000)
    assert p == approx(0.031, rel=0.01)


# def test_probability_of_ththh2():
#     e = Experiment()
#     p = e.flip_coin_with_pattern_n_times([0, 1, 0, 1, 1], 1_000_000, 5)
#     assert p == approx((0.5)**5, rel=0.01)


def test_probability_of_dice_odd34l3():
    e = Experiment()
    patterns = [[1, 3, 4, 1], [1, 3, 4, 2], [3, 3, 4, 1], [3, 3, 4, 2], [5, 3, 4, 1], [5, 3, 4, 2]]
    p = e.roll_dice_4x_times(patterns, 1000, 4)
    assert p == approx(0.45 * 0.05 * 0.3 * 0.35, rel=0.01)


def test_probability_of_box_draws():
    e = Experiment()
    patterns = ['red', 'green', 'yellow', 'red', 'red']
    p = e.draw_marbles_from_box(patterns, 5, 1000000)
    assert p == approx(0.0095, rel=0.01)

# def test_probability_of_hhhh():
#     e = Experiment()
#     p = e.biased_flip_coin_with_pattern_n_times([1, 1, 1, 1], 1_000_000, 4)
#     assert p == approx((0.3)**4, rel=0.01)
