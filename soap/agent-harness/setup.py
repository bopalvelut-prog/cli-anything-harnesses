from setuptools import setup
setup(
    name='cli-anything-soap',
    version='1.0.0',
    packages=['cli_anything.soap'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-soap=cli_anything.soap:cli']},
)
