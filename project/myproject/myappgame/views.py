from django.http import HttpResponse
from random import randint
import logging

logger = logging.getLogger(__name__)


def coin(request):
    side = ['avers', 'reverse'][randint(0, 1)]
    logger.info(f'coinplay requested; coin side: {side}')
    return HttpResponse(f"Coin side: {side}")


def dice(request):
    cube_side = randint(1, 6)
    logger.info(f'diceplay requested; cube-side: {cube_side}')
    return HttpResponse(f"Cube side: {cube_side}")


def random_number(request):
    answer = randint(0, 100)
    logger.info(f'random_number requested; answer: {answer}')
    return HttpResponse(f"Random number: {answer}")