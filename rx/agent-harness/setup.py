from setuptools import setup
setup(
    name='cli-anything-rx',
    version='1.0.0',
    packages=['cli_anything.rx'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rx=cli_anything.rx:cli']},
)
