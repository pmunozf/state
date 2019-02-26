#!/usr/bin/env python
#
# Pablo Munoz (c) 2019
# pablo.bmf@gmail.com
#
# Facilities for state management
import inspect
from pprint import pprint as print

class State:

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

