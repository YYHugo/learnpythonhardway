from nose.tools import *
import printARGS


def setup():
    print("SETUP!")


def teardown():
    print("Tear DOWN!")


def test_basic():
    print("I RAN!")
    