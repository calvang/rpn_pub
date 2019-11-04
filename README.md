# rpn_pub
![Build Status](https://travis-ci.org/calvang/rpn_pub.svg?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/calvang/rpn_pub/badge.svg?branch=master)](https://coveralls.io/github/calvang/rpn_pub?branch=master)

**Table of Contents:**

[TOC]

### Setup

*Notes*

- Does not work on ssh or WSL (works on WSL2) due to tkinter
- Install tkinter if not already included with python
  - Use the command `$ sudo apt-get install python-tk`
- Use python3.5 or higher (tkinter is python3-dependent)
- Make sure you have pip3 installed or run pip with python3 instead

1) To install all dependencies, use the command `$ pip3 install -r requirements.txt`

- If your machine has both python3 and python2 installed and does not recognize the `pip3` command, try using `$sudo python3 -m pip install -r requirements.txt`

2) To run:  `$ python3 rpn.py`

### Testing

To run the full testing suite:

`$ python3 -m unittest`

or 

`$ python3 test_rpn.py`



