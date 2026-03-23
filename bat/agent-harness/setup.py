from setuptools import setup
setup(
    name='cli-anything-bat',
    version='1.0.0',
    packages=['cli_anything.bat'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bat=cli_anything.bat:cli']},
)
