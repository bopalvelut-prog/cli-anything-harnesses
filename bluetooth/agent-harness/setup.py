from setuptools import setup
setup(
    name='cli-anything-bluetooth',
    version='1.0.0',
    packages=['cli_anything.bluetooth'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bluetooth=cli_anything.bluetooth:cli']},
)
