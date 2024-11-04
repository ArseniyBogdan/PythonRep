import enum
import time
from collections import OrderedDict


class CacheStrategyEnum(enum.Enum):
    fifo = 1
    lifo = 2


def memoize(max_size: int = 128, cache_strategy: CacheStrategyEnum = CacheStrategyEnum.lifo):
    def outer_wrapper(func):
        cache = {}

        # получаем кэш для текущей функции, если его нет то создаём
        if func.__name__ in cache:
            func_cache = cache[func.__name__]
        else:
            cache[func.__name__] = OrderedDict()
            func_cache = cache[func.__name__]

        def inner_wrapper(*args, **kwargs):
            # Проверяем, есть ли значение в кэше, если есть -> возвращаем,
            # иначе вычисляем значение и добавляем его в кэш
            if args in func_cache:
                return func_cache[args]
            else:
                # тут удаляем один элемент из списка в зависимости от стратегии, если max_size может быть превышен
                if len(func_cache) + 1 > 128 and cache_strategy == CacheStrategyEnum.lifo:
                    func_cache.popitem(last=True)
                if len(func_cache) + 1 > 128 and cache_strategy == CacheStrategyEnum.fifo:
                    func_cache.popitem(last=False)

                func_cache[args] = func(*args)
                print(func_cache, end="\n")
                return func_cache[args]
        return inner_wrapper
    return outer_wrapper


@memoize()
def foo(arg: int) -> str:
    # надо раскомментировать перед запуском этого теста
    # time.sleep(3.0)
    return "Hello: {}".format(arg)


def test1():
    print(foo(1), end="\n")
    print(foo(1), end="\n")
    print(foo(2), end="\n")


def test2():
    for i in range(140):
        print(foo(i), end="\n")


if __name__ == '__main__':
    # test1()
    test2()
