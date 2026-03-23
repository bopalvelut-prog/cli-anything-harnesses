from setuptools import setup
setup(
    name='cli-anything-core',
    version='1.0.0',
    packages=['cli_anything.core'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-core=cli_anything.core:cli']},
)
