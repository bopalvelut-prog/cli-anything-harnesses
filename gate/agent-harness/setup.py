from setuptools import setup
setup(
    name='cli-anything-gate',
    version='1.0.0',
    packages=['cli_anything.gate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gate=cli_anything.gate:cli']},
)
