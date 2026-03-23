from setuptools import setup
setup(
    name='cli-anything-javadoc',
    version='1.0.0',
    packages=['cli_anything.javadoc'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-javadoc=cli_anything.javadoc:cli']},
)
