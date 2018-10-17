import inspect
import pkg_resources
from os import path


def get_abs_path(depth=1):
    """
    Get the absolute path of the specified entry in the stack

    :param int depth: How far down the stack to look. Defaults to 1
    :return: Absolute path or None if any error
    :rtype: str
    """
    # Always start in a known place
    frames = inspect.stack()
    try:
        if 0 < depth <= len(frames):
            frame = frames[depth - 1]
            abs_path = frame.filename
        else:
            abs_path = None
    finally:
        for frame in frames:
            del frame

    return abs_path


def guess_package(current_dir=None, depth=1):
    """
    Guess the current package.

    If the current file is not in a package, recurse up the stack
    until the first package directory is found

    :param str current_dir: Starting directory. Default is None.
    :param int depth: How far up the stack to recurse. Default is 1
    :return: Package name or None
    :rtype: str
    """
    if not current_dir:
        # Need to figure the call depth manually
        # Depends on calling sequence in this module
        new_depth = depth + 2
        abs_path = get_abs_path(depth=new_depth)
        current_dir = path.dirname(abs_path)
    init_py_path = path.normpath(path.join(current_dir, '__init__.py'))
    if path.exists(init_py_path):
        package = path.basename(current_dir)
        return package
    else:
        parent_dir, last_path = path.split(current_dir)
        if parent_dir == '/':
            return None
        return guess_package(depth=depth+1)


def get_package_path(package_name=None):
    package_name = package_name if package_name else guess_package()
    possible_path = pkg_resources.resource_filename(package_name, '/')
    possible_path = path.normpath(possible_path)
    return possible_path if path.exists(possible_path) else None


def get_data_path(file_name=None, data_directory_name='data', package_name=None):
    if file_name:
        possible_path = pkg_resources.resource_filename(guess_package(package_name),
            "{0}/{1}".format(data_directory_name,file_name))
    else:
        possible_path = pkg_resources.resource_filename(guess_package(package_name),
            "{0}/".format(data_directory_name))
    possible_path = path.normpath(possible_path)
    return possible_path if path.exists(possible_path) else None


if __name__ == '__main__':
    print(get_abs_path())
    print(guess_package())
    print(get_package_path())
    print(get_data_path())

