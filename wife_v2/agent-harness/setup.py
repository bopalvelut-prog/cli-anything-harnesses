from setuptools import setup
setup(
    name='cli-anything-wife_v2',
    version='1.0.0',
    packages=['cli_anything.wife_v2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wife_v2=cli_anything.wife_v2:cli']},
)
