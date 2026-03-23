from setuptools import setup
setup(
    name='cli-anything-lose',
    version='1.0.0',
    packages=['cli_anything.lose'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lose=cli_anything.lose:cli']},
)
