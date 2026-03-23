from setuptools import setup
setup(
    name='cli-anything-aspectj',
    version='1.0.0',
    packages=['cli_anything.aspectj'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aspectj=cli_anything.aspectj:cli']},
)
