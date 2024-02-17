import lab6q1
from io import StringIO
from sys import stderr
def test_case1(monkeypatch, capsys):
    number_inputs = StringIO('5\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab6q1.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'5 times 12 =  60') != -1

def test_case2(monkeypatch, capsys):
  with open(f"lab6q1.py") as tf:
    head = [next(tf) for _ in range(25)]
    s = tf.read()
    assert(s.find("for") != -1 )
    assert(s.find("range") != -1 )
    assert(s.find("while") == -1 )

