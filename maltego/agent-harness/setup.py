from setuptools import setup
setup(
    name='cli-anything-maltego',
    version='1.0.0',
    packages=['cli_anything.maltego'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-maltego=cli_anything.maltego:cli']},
)
