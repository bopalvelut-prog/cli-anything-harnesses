from setuptools import setup
setup(
    name='cli-anything-nearby',
    version='1.0.0',
    packages=['cli_anything.nearby'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nearby=cli_anything.nearby:cli']},
)
