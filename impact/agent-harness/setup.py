from setuptools import setup
setup(
    name='cli-anything-impact',
    version='1.0.0',
    packages=['cli_anything.impact'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-impact=cli_anything.impact:cli']},
)
