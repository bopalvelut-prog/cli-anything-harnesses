from setuptools import setup
setup(
    name='cli-anything-operation',
    version='1.0.0',
    packages=['cli_anything.operation'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-operation=cli_anything.operation:cli']},
)
