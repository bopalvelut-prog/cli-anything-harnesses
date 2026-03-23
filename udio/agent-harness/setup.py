from setuptools import setup
setup(
    name='cli-anything-udio',
    version='1.0.0',
    packages=['cli_anything.udio'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-udio=cli_anything.udio:cli']},
)
