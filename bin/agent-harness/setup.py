from setuptools import setup
setup(
    name='cli-anything-bin',
    version='1.0.0',
    packages=['cli_anything.bin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bin=cli_anything.bin:cli']},
)
