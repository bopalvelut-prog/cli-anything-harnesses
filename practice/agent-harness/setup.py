from setuptools import setup
setup(
    name='cli-anything-practice',
    version='1.0.0',
    packages=['cli_anything.practice'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-practice=cli_anything.practice:cli']},
)
