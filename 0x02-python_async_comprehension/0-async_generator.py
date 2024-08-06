#!/usr/bin/env python3

""" Async Comprehensions. """

from asyncio import sleep
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Yields a random float between 0 and 10 after sleeping for 1 second, 10 times. """
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
