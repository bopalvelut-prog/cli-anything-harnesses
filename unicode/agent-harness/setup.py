from setuptools import setup
setup(
    name='cli-anything-unicode',
    version='1.0.0',
    packages=['cli_anything.unicode'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-unicode=cli_anything.unicode:cli']},
)
