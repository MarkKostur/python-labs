import pytest
from task7 import charivna_kulka, charivna_kulka_changed_chances

answers = ['yes', 'no', 'maybe']

# Перевірка чи тип поверненого результату є стрічкою
def test_type_result_func():
    assert isinstance(charivna_kulka('is putin dead?', answers), str)

@pytest.mark.parametrize('question,expected', [
    ('', 'it is not a question'),
    ('Is putin dead?', ('yes', 'no', 'maybe')),
    ('__39210131', 'it is not a question'),
])

def test_charivna_kulka(question, expected):
    assert charivna_kulka(question, answers) in expected

@pytest.mark.parametrize('question,expected', [
  ('will Ukraine win in this war?', 'yes')  
])

def test_charivna_kulka_changed_chances(question, expected):
    assert charivna_kulka_changed_chances(question, [(0, 1), (1, 0), (2, 0)], answers) in expected