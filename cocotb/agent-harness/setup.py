from setuptools import setup
setup(
    name='cli-anything-cocotb',
    version='1.0.0',
    packages=['cli_anything.cocotb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cocotb=cli_anything.cocotb:cli']},
)
