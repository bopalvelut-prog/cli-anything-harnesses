from setuptools import setup
setup(
    name='cli-anything-coroutine',
    version='1.0.0',
    packages=['cli_anything.coroutine'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-coroutine=cli_anything.coroutine:cli']},
)
