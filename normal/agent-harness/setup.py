from setuptools import setup
setup(
    name='cli-anything-normal',
    version='1.0.0',
    packages=['cli_anything.normal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-normal=cli_anything.normal:cli']},
)
