from setuptools import setup
setup(
    name='cli-anything-know',
    version='1.0.0',
    packages=['cli_anything.know'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-know=cli_anything.know:cli']},
)
