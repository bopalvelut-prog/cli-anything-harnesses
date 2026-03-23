from setuptools import setup
setup(
    name='cli-anything-fortigate',
    version='1.0.0',
    packages=['cli_anything.fortigate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fortigate=cli_anything.fortigate:cli']},
)
