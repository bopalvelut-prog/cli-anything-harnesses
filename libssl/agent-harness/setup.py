from setuptools import setup
setup(
    name='cli-anything-libssl',
    version='1.0.0',
    packages=['cli_anything.libssl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-libssl=cli_anything.libssl:cli']},
)
