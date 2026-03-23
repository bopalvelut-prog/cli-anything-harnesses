from setuptools import setup
setup(
    name='cli-anything-undergo',
    version='1.0.0',
    packages=['cli_anything.undergo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-undergo=cli_anything.undergo:cli']},
)
