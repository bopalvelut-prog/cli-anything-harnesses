from setuptools import setup
setup(
    name='cli-anything-panda',
    version='1.0.0',
    packages=['cli_anything.panda'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-panda=cli_anything.panda:cli']},
)
