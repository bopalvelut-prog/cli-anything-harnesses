from setuptools import setup
setup(
    name='cli-anything-mountain',
    version='1.0.0',
    packages=['cli_anything.mountain'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mountain=cli_anything.mountain:cli']},
)
