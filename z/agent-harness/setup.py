from setuptools import setup
setup(
    name='cli-anything-z',
    version='1.0.0',
    packages=['cli_anything.z'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-z=cli_anything.z:cli']},
)
