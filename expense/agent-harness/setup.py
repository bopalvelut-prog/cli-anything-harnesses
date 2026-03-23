from setuptools import setup
setup(
    name='cli-anything-expense',
    version='1.0.0',
    packages=['cli_anything.expense'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-expense=cli_anything.expense:cli']},
)
