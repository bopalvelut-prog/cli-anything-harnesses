from setuptools import setup
setup(
    name='cli-anything-clion',
    version='1.0.0',
    packages=['cli_anything.clion'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-clion=cli_anything.clion:cli']},
)
