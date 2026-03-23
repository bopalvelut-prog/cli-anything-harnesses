from setuptools import setup
setup(
    name='cli-anything-bath',
    version='1.0.0',
    packages=['cli_anything.bath'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bath=cli_anything.bath:cli']},
)
