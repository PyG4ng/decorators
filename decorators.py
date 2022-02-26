import logging


def decorator(path):
    logging.basicConfig(filename=path, level=logging.INFO,
                        format='%(asctime)s | %(levelname)s | %(message)s')

    def outer(foo):

        def inner(*args, **kwargs):
            result = foo(*args, **kwargs)
            logging.info(f'Function: {foo.__name__} | Arguments: {args} {kwargs} | Results: \n{result}')
            return result

        return inner

    return outer


@decorator('logs.log')
def calculate(a, b, c):
    return a + b * c


if __name__ == '__main__':
    calculate(2, 4, 8)
