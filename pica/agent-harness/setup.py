from setuptools import setup
setup(
    name='cli-anything-pica',
    version='1.0.0',
    packages=['cli_anything.pica'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pica=cli_anything.pica:cli']},
)
