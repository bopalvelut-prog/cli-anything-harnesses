from setuptools import setup
setup(
    name='cli-anything-deposit',
    version='1.0.0',
    packages=['cli_anything.deposit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-deposit=cli_anything.deposit:cli']},
)
