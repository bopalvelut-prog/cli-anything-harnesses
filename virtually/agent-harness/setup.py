from setuptools import setup
setup(
    name='cli-anything-virtually',
    version='1.0.0',
    packages=['cli_anything.virtually'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-virtually=cli_anything.virtually:cli']},
)
