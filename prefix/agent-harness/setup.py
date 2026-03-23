from setuptools import setup
setup(
    name='cli-anything-prefix',
    version='1.0.0',
    packages=['cli_anything.prefix'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prefix=cli_anything.prefix:cli']},
)
