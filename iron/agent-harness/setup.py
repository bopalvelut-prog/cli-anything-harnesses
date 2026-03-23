from setuptools import setup
setup(
    name='cli-anything-iron',
    version='1.0.0',
    packages=['cli_anything.iron'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-iron=cli_anything.iron:cli']},
)
