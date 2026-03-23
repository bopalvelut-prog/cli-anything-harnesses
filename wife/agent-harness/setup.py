from setuptools import setup
setup(
    name='cli-anything-wife',
    version='1.0.0',
    packages=['cli_anything.wife'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wife=cli_anything.wife:cli']},
)
