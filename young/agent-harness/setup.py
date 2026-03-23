from setuptools import setup
setup(
    name='cli-anything-young',
    version='1.0.0',
    packages=['cli_anything.young'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-young=cli_anything.young:cli']},
)
