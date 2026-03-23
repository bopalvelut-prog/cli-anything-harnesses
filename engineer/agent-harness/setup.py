from setuptools import setup
setup(
    name='cli-anything-engineer',
    version='1.0.0',
    packages=['cli_anything.engineer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-engineer=cli_anything.engineer:cli']},
)
