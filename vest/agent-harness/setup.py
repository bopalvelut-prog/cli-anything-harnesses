from setuptools import setup
setup(
    name='cli-anything-vest',
    version='1.0.0',
    packages=['cli_anything.vest'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vest=cli_anything.vest:cli']},
)
