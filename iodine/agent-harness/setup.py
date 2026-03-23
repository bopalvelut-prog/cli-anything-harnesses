from setuptools import setup
setup(
    name='cli-anything-iodine',
    version='1.0.0',
    packages=['cli_anything.iodine'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-iodine=cli_anything.iodine:cli']},
)
