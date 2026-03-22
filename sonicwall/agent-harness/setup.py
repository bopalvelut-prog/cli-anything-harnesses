from setuptools import setup
setup(
    name='cli-anything-sonicwall',
    version='1.0.0',
    packages=['cli_anything.sonicwall'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sonicwall=cli_anything.sonicwall:cli']},
)
