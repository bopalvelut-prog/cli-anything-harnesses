from setuptools import setup
setup(
    name='cli-anything-nist',
    version='1.0.0',
    packages=['cli_anything.nist'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nist=cli_anything.nist:cli']},
)
