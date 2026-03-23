from setuptools import setup
setup(
    name='cli-anything-wttrin',
    version='1.0.0',
    packages=['cli_anything.wttrin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wttrin=cli_anything.wttrin:cli']},
)
