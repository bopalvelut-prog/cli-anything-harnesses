from setuptools import setup
setup(
    name='cli-anything-antmedia',
    version='1.0.0',
    packages=['cli_anything.antmedia'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-antmedia=cli_anything.antmedia:cli']},
)
