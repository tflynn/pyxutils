from setuptools import setup, find_packages

setup(name='pyxutils',
      version='0.2',
      description='',
      url='https://github.com/tflynn/pyxutils.git',
      author='Tracy Flynn',
      author_email='tracysflynn@gmail.com',
      license='MIT',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      install_requires=[],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
