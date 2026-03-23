from setuptools import setup
setup(
    name='cli-anything-budget',
    version='1.0.0',
    packages=['cli_anything.budget'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-budget=cli_anything.budget:cli']},
)
