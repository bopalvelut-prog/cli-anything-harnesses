from setuptools import setup
setup(
    name='cli-anything-outcome',
    version='1.0.0',
    packages=['cli_anything.outcome'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-outcome=cli_anything.outcome:cli']},
)
