from setuptools import setup
setup(
    name='cli-anything-better_sqlite',
    version='1.0.0',
    packages=['cli_anything.better_sqlite'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-better_sqlite=cli_anything.better_sqlite:cli']},
)
