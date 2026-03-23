from setuptools import setup
setup(
    name='cli-anything-distribute',
    version='1.0.0',
    packages=['cli_anything.distribute'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-distribute=cli_anything.distribute:cli']},
)
