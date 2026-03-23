from setuptools import setup
setup(
    name='cli-anything-swing',
    version='1.0.0',
    packages=['cli_anything.swing'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-swing=cli_anything.swing:cli']},
)
