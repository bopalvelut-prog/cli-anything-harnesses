from setuptools import setup
setup(
    name='cli-anything-control',
    version='1.0.0',
    packages=['cli_anything.control'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-control=cli_anything.control:cli']},
)
