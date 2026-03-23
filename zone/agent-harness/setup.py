from setuptools import setup
setup(
    name='cli-anything-zone',
    version='1.0.0',
    packages=['cli_anything.zone'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zone=cli_anything.zone:cli']},
)
