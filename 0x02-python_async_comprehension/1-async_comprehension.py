#!/usr/bin/env python3

""" Async Comprehensions. """

from asyncio import sleep
from random import uniform
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Collects and returns a list of floats generated asynchronously. """
    return [i async for i in async_generator()]
