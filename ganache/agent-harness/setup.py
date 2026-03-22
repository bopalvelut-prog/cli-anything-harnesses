from setuptools import setup
setup(
    name='cli-anything-ganache',
    version='1.0.0',
    packages=['cli_anything.ganache'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ganache=cli_anything.ganache:cli']},
)
