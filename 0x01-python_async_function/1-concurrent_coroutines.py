#!/usr/bin/env python3
'''
Contains a coroutine.
'''
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''that takes in 2 int arguments'''
    r = await asyncio.gather(*(wait_random(max_delay) for x in range(n)))
    return sorted(r)
