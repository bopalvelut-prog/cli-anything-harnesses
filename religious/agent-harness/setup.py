from setuptools import setup
setup(
    name='cli-anything-religious',
    version='1.0.0',
    packages=['cli_anything.religious'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-religious=cli_anything.religious:cli']},
)
