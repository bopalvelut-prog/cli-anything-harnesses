from setuptools import setup
setup(
    name='cli-anything-case',
    version='1.0.0',
    packages=['cli_anything.case'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-case=cli_anything.case:cli']},
)
