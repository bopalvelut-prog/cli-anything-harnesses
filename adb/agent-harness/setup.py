from setuptools import setup
setup(
    name='cli-anything-adb',
    version='1.0.0',
    packages=['cli_anything.adb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-adb=cli_anything.adb:cli']},
)
