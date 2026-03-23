from setuptools import setup
setup(
    name='cli-anything-beneath',
    version='1.0.0',
    packages=['cli_anything.beneath'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-beneath=cli_anything.beneath:cli']},
)
