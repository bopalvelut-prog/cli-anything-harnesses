from setuptools import setup
setup(
    name='cli-anything-begin',
    version='1.0.0',
    packages=['cli_anything.begin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-begin=cli_anything.begin:cli']},
)
