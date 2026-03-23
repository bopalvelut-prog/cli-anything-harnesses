from setuptools import setup
setup(
    name='cli-anything-capacity',
    version='1.0.0',
    packages=['cli_anything.capacity'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-capacity=cli_anything.capacity:cli']},
)
