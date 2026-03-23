from setuptools import setup
setup(
    name='cli-anything-native',
    version='1.0.0',
    packages=['cli_anything.native'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-native=cli_anything.native:cli']},
)
