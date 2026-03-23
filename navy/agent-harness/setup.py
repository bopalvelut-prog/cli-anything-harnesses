from setuptools import setup
setup(
    name='cli-anything-navy',
    version='1.0.0',
    packages=['cli_anything.navy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-navy=cli_anything.navy:cli']},
)
