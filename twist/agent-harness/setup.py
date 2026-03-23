from setuptools import setup
setup(
    name='cli-anything-twist',
    version='1.0.0',
    packages=['cli_anything.twist'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-twist=cli_anything.twist:cli']},
)
