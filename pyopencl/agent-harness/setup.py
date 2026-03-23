from setuptools import setup
setup(
    name='cli-anything-pyopencl',
    version='1.0.0',
    packages=['cli_anything.pyopencl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pyopencl=cli_anything.pyopencl:cli']},
)
