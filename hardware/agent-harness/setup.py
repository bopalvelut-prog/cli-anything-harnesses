from setuptools import setup
setup(
    name='cli-anything-hardware',
    version='1.0.0',
    packages=['cli_anything.hardware'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hardware=cli_anything.hardware:cli']},
)
