from setuptools import setup
setup(
    name='cli-anything-mockery',
    version='1.0.0',
    packages=['cli_anything.mockery'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mockery=cli_anything.mockery:cli']},
)
