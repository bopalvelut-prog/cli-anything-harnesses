from setuptools import setup
setup(
    name='cli-anything-fly',
    version='1.0.0',
    packages=['cli_anything.fly'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fly=cli_anything.fly:cli']},
)
