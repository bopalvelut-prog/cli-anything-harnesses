from setuptools import setup
setup(
    name='cli-anything-severity',
    version='1.0.0',
    packages=['cli_anything.severity'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-severity=cli_anything.severity:cli']},
)
