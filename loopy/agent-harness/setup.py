from setuptools import setup
setup(
    name='cli-anything-loopy',
    version='1.0.0',
    packages=['cli_anything.loopy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-loopy=cli_anything.loopy:cli']},
)
