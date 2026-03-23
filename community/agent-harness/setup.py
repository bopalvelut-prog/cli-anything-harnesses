from setuptools import setup
setup(
    name='cli-anything-community',
    version='1.0.0',
    packages=['cli_anything.community'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-community=cli_anything.community:cli']},
)
