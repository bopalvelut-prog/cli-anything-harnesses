from setuptools import setup
setup(
    name='cli-anything-pytest_django',
    version='1.0.0',
    packages=['cli_anything.pytest_django'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pytest_django=cli_anything.pytest_django:cli']},
)
