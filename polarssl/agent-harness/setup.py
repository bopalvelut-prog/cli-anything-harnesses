from setuptools import setup
setup(
    name='cli-anything-polarssl',
    version='1.0.0',
    packages=['cli_anything.polarssl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-polarssl=cli_anything.polarssl:cli']},
)
