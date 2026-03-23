from setuptools import setup
setup(
    name='cli-anything-oxidized',
    version='1.0.0',
    packages=['cli_anything.oxidized'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-oxidized=cli_anything.oxidized:cli']},
)
