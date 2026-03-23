from setuptools import setup
setup(
    name='cli-anything-stamina',
    version='1.0.0',
    packages=['cli_anything.stamina'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stamina=cli_anything.stamina:cli']},
)
