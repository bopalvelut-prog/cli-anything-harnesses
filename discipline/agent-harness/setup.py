from setuptools import setup
setup(
    name='cli-anything-discipline',
    version='1.0.0',
    packages=['cli_anything.discipline'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-discipline=cli_anything.discipline:cli']},
)
