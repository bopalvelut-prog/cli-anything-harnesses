from setuptools import setup
setup(
    name='cli-anything-fifteen',
    version='1.0.0',
    packages=['cli_anything.fifteen'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fifteen=cli_anything.fifteen:cli']},
)
