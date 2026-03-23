from setuptools import setup
setup(
    name='cli-anything-front',
    version='1.0.0',
    packages=['cli_anything.front'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-front=cli_anything.front:cli']},
)
