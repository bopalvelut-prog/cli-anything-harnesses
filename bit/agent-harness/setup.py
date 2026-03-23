from setuptools import setup
setup(
    name='cli-anything-bit',
    version='1.0.0',
    packages=['cli_anything.bit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bit=cli_anything.bit:cli']},
)
