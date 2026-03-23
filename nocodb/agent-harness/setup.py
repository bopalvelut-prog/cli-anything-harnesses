from setuptools import setup
setup(
    name='cli-anything-nocodb',
    version='1.0.0',
    packages=['cli_anything.nocodb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nocodb=cli_anything.nocodb:cli']},
)
