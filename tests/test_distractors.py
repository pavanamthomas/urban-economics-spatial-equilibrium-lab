from urbaneq.distractors import CORRECT_KEY, OPTIONS


def test_distractors_are_ten_letters_one_key() -> None:
    assert list(OPTIONS) == list("ABCDEFGHIJ")
    assert CORRECT_KEY == "B"
    assert CORRECT_KEY in OPTIONS
