from setuptools import setup
setup(
    name='cli-anything-tip',
    version='1.0.0',
    packages=['cli_anything.tip'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tip=cli_anything.tip:cli']},
)
