from setuptools import setup
setup(
    name='cli-anything-lovely',
    version='1.0.0',
    packages=['cli_anything.lovely'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lovely=cli_anything.lovely:cli']},
)
