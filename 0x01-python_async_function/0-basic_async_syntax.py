#!/usr/bin/env python3
'''asyncio'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''given argument'''
    n = random.uniform(0, max_delay)
    await asyncio.sleep(n)
    return n
