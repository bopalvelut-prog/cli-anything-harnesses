from setuptools import setup
setup(
    name='cli-anything-satellite',
    version='1.0.0',
    packages=['cli_anything.satellite'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-satellite=cli_anything.satellite:cli']},
)
