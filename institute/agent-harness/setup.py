from setuptools import setup
setup(
    name='cli-anything-institute',
    version='1.0.0',
    packages=['cli_anything.institute'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-institute=cli_anything.institute:cli']},
)
