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
    """
    Get the absolute path for a package

    Only appears to work for packages at the root.

    :param str package_name: Package name
    :return: Package name or None
    :rtype: str
    """
    package_name = package_name if package_name else guess_package()
    resource_path = pkg_resources.resource_filename(package_name, '/')
    resource_path = path.normpath(resource_path)
    return resource_path if path.exists(resource_path) else None


def get_data_path(file_name=None, data_directory_name='data', package_name=None):
    """
    Get the path to a file in data directory for a package (<package>/data/<filename>).

    Only appears to work for packages at the root.

    :param str file_name: File name in data directory
    :param str data_directory_name: package/directory (below root)
    :param str package_name: Package name
    :return: Directory or file path or None
    :rtype: str
    """
    package_name = package_name if package_name else guess_package()
    package_path = get_package_path(package_name=package_name)
    if package_path:
        base_data_path = path.normpath(path.join(package_path, data_directory_name))
        if file_name:
            resource_path = path.normpath(path.join(base_data_path, file_name))
        else:
            resource_path = base_data_path

        return resource_path if path.exists(resource_path) else None

    else:
        return None


if __name__ == '__main__':
    print(get_abs_path())
    print(guess_package())
    print(get_package_path())
    print(get_data_path())

