import argparse
from os import path
import os
import re

test_file_regex = re.compile(r'test_(.*)\.py')


def list_default_targets() -> list[str]:
    # get filename like test_***.py
    return [test_file_regex.match(f).group(1) for f in os.listdir(path.join(path.dirname(__file__), '..', 'tests')) if test_file_regex.match(f) and f != 'test_utils.py']


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # targets default all
    parser.add_argument('targets', nargs='*', help='test targets')
    # verbose output for pytest
    parser.add_argument('--verbose', '-v', action='store_true', help='verbose output')

    args = parser.parse_args()

    print(args)

    pytest_args = []
    targets = args.targets if args.targets else list_default_targets()

    for target in targets:
        target_path = path.join(path.dirname(__file__), 'test_{}.py'.format(target))
        if path.exists(target_path):
            pytest_args.append(target_path)
        else:
            assert False, 'Test target {} not found'.format(target)

    if args.verbose:
        pytest_args.append('-s')

    import pytest
    exit(int(pytest.main(pytest_args)))
