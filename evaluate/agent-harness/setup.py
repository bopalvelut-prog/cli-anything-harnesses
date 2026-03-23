from setuptools import setup
setup(
    name='cli-anything-evaluate',
    version='1.0.0',
    packages=['cli_anything.evaluate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-evaluate=cli_anything.evaluate:cli']},
)
