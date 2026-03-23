from setuptools import setup
setup(
    name='cli-anything-rock',
    version='1.0.0',
    packages=['cli_anything.rock'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rock=cli_anything.rock:cli']},
)
