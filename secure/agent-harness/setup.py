from setuptools import setup
setup(
    name='cli-anything-secure',
    version='1.0.0',
    packages=['cli_anything.secure'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-secure=cli_anything.secure:cli']},
)
