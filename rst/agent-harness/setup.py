from setuptools import setup
setup(
    name='cli-anything-rst',
    version='1.0.0',
    packages=['cli_anything.rst'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rst=cli_anything.rst:cli']},
)
