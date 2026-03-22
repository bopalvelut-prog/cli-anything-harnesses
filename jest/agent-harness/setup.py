from setuptools import setup
setup(
    name='cli-anything-jest',
    version='1.0.0',
    packages=['cli_anything.jest'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jest=cli_anything.jest:cli']},
)
