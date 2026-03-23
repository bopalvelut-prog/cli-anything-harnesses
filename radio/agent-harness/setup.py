from setuptools import setup
setup(
    name='cli-anything-radio',
    version='1.0.0',
    packages=['cli_anything.radio'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-radio=cli_anything.radio:cli']},
)
