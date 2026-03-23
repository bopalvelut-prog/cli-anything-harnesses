from setuptools import setup
setup(
    name='cli-anything-letter',
    version='1.0.0',
    packages=['cli_anything.letter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-letter=cli_anything.letter:cli']},
)
