from lib.grammar import *
import pytest


# test for if there is a capital at the start
def test_text_for_capital_at_start_and_full_stop_at_end():
    gs = GrammarStats()
    results = gs.check("Hello.")
    assert results == True


# test for punctuation at end '!'
def test_text_for_capital_at_start_and_exclamation_at_end():
    gs = GrammarStats()
    results = gs.check("Hello!")
    assert results == True


# test for punctuation at end '?'
def test_text_for_capital_at_start_and_question_mark_at_end():
    gs = GrammarStats()
    results = gs.check("Hello?")
    assert results == True


# test of no capital or no punctuation returns false
def test_text_for_no_capital_at_start_and_punctuation_at_end():
    gs = GrammarStats()
    results = gs.check("hello")
    assert results == False


# test capital with no punctuation returns false
def test_text_for_capital_at_start_and__no_punctuation_at_end():
    gs = GrammarStats()
    results = gs.check("Hello")
    assert results == False


# test punctuation with no capital returns false
def test_text_for_no_capital_at_start_and_with_punctuation_at_end():
    gs = GrammarStats()
    results = gs.check("hello.")
    assert results == False


# test non-string as argument
def test_incorrect_data_type_entry():
    gs = GrammarStats()
    result = gs.check(0)
    assert result == False


# test return false if input is an empty string
def test_empty_string_returns_false():
    gs = GrammarStats()
    result = gs.check("")
    assert result == False


# test output is 100% if all checks have passed as true
def test_all_grammar_is_correct_returns_100():
    gs = GrammarStats()
    gs.check("Hello.")
    gs.check("Hello!")
    gs.check("Hello?")
    assert gs.percentage_good() == 100


# test if all grammar is incorrect - return 0
def test_all_grammar_is_incorrect_returns_100():
    gs = GrammarStats()
    gs.check("Hello")
    gs.check("hello!")
    gs.check("hello")
    assert gs.percentage_good() == 0


# test mixed results return false - 1/2 returns 50
def test_half_grammar_is_incorrect_returns_100():
    gs = GrammarStats()
    gs.check("Hello.")
    gs.check("Hello!")
    gs.check("hello")
    gs.check("helLO")
    assert gs.percentage_good() == 50


# test for 33% return
def test_some_grammar_is_incorrect_returns_100():
    gs = GrammarStats()
    gs.check("Hello.")
    gs.check("hello!")
    gs.check("hello")
    assert gs.percentage_good() == 33


# test raise exception if no checks completed
def test_raises_excpetion_if_calls_to_check():
    gs = GrammarStats()
    with pytest.raises(Exception) as err:
        result = gs.percentage_good()
    assert str(err.value) == "No checks completed"
