from setuptools import setup
setup(
    name='cli-anything-capture',
    version='1.0.0',
    packages=['cli_anything.capture'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-capture=cli_anything.capture:cli']},
)
