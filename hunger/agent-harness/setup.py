from setuptools import setup
setup(
    name='cli-anything-hunger',
    version='1.0.0',
    packages=['cli_anything.hunger'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hunger=cli_anything.hunger:cli']},
)
