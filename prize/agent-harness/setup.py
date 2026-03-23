from setuptools import setup
setup(
    name='cli-anything-prize',
    version='1.0.0',
    packages=['cli_anything.prize'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prize=cli_anything.prize:cli']},
)
