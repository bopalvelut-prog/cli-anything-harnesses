from setuptools import setup
setup(
    name='cli-anything-unlikely',
    version='1.0.0',
    packages=['cli_anything.unlikely'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-unlikely=cli_anything.unlikely:cli']},
)
