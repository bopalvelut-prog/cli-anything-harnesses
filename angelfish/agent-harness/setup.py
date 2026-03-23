from setuptools import setup
setup(
    name='cli-anything-angelfish',
    version='1.0.0',
    packages=['cli_anything.angelfish'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-angelfish=cli_anything.angelfish:cli']},
)
