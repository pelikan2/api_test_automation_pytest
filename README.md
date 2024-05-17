# api_test_automation_pytest

This framework is written in my favorite combo python pytest.

# Setup

1. Clone project to your favourite IDE: https://github.com/pelikan2/api_test_automation_pytest.git
2. In file requirements.txt are all necessary packages, so in terminal paste this command:

<br>MacOS: pip3 install -r requirements.txt </br>
<br>Windows: pip install -r requirements.txt </br>

# Project structure

Project consists from two python packages (Tests, Utils), in package Tests is module with testcases, in package Utils is
module with support functions and some constants.
To run testcases you need to paste this command:

- **pytest Tests/test_scenarios.py -s -v** - I personally prefer this command.
