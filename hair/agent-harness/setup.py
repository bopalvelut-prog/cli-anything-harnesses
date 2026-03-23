from setuptools import setup
setup(
    name='cli-anything-hair',
    version='1.0.0',
    packages=['cli_anything.hair'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hair=cli_anything.hair:cli']},
)
