from setuptools import setup
setup(
    name='cli-anything-stupid',
    version='1.0.0',
    packages=['cli_anything.stupid'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stupid=cli_anything.stupid:cli']},
)
