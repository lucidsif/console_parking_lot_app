import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from console_app import display_title_bar

def test_display_title_bar(capsys): # or use "capfd" for fd-level
    display_title_bar()
    captured = capsys.readouterr()
    line1 = "\t**********************************************\n"
    line2 = "\t**  Welcome to Sif's parking lot program!  **\n"
    line3 = "\t*******     How can we help you?      *******\n"
    line4 = "\t**********************************************\n"
    expectedPrint = line1 + line2 + line3 + line4 + '\n'
    assert captured.out == expectedPrint