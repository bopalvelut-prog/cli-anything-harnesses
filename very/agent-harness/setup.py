from setuptools import setup
setup(
    name='cli-anything-very',
    version='1.0.0',
    packages=['cli_anything.very'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-very=cli_anything.very:cli']},
)
