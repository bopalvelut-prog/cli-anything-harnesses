from setuptools import setup
setup(
    name='cli-anything-while',
    version='1.0.0',
    packages=['cli_anything.while'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-while=cli_anything.while:cli']},
)
