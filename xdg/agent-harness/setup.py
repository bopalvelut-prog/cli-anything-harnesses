from setuptools import setup
setup(
    name='cli-anything-xdg',
    version='1.0.0',
    packages=['cli_anything.xdg'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-xdg=cli_anything.xdg:cli']},
)
