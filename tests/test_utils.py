
from functools import wraps
import importlib.util
import os
import sys

test_dir_mapping = {
    'c_cpp': 'C_CPP',
    'python': 'Python',
    'java': 'Java',
    'rust': 'Rust',
    'javascript': 'JavaScript',
    'js': 'JavaScript'
}


def generate_compile_and_run():
    def decorator(func):
        test_name = func.__name__.replace('test_', '').lower()
        if test_name not in test_dir_mapping:
            raise Exception('No test module found for target {}'.format(test_name))
        py_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..',
                                  test_dir_mapping[test_name], 'compile_and_run.py'))
        dir_path = os.path.dirname(py_path)
        if not os.path.exists(py_path):
            raise Exception('No test module found for target {}'.format(test_name))

        def wrap_func(*args, **kwargs):
            spec = importlib.util.spec_from_file_location('compile_and_run', py_path)
            compile_and_run = importlib.util.module_from_spec(spec)
            os.chdir(dir_path)
            sys.path.append(dir_path)
            spec.loader.exec_module(compile_and_run)
            assert compile_and_run.compile_program()[0]
            assert compile_and_run.render_gif(os.path.join(dir_path, '..', 'result.gif'))[0]
            return func(*args, **kwargs)
        return wrap_func

    return decorator
