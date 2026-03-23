from setuptools import setup
setup(
    name='cli-anything-classfile',
    version='1.0.0',
    packages=['cli_anything.classfile'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-classfile=cli_anything.classfile:cli']},
)
