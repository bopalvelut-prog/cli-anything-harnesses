from setuptools import setup
setup(
    name='cli-anything-furniture',
    version='1.0.0',
    packages=['cli_anything.furniture'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-furniture=cli_anything.furniture:cli']},
)
