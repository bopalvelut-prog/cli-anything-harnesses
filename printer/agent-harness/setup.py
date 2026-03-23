from setuptools import setup
setup(
    name='cli-anything-printer',
    version='1.0.0',
    packages=['cli_anything.printer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-printer=cli_anything.printer:cli']},
)
