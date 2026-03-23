from setuptools import setup
setup(
    name='cli-anything-jest_v2',
    version='1.0.0',
    packages=['cli_anything.jest_v2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jest_v2=cli_anything.jest_v2:cli']},
)
