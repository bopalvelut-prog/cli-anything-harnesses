from setuptools import setup
setup(
    name='cli-anything-conftest',
    version='1.0.0',
    packages=['cli_anything.conftest'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-conftest=cli_anything.conftest:cli']},
)
