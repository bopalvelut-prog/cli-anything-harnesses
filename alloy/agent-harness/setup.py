from setuptools import setup
setup(
    name='cli-anything-alloy',
    version='1.0.0',
    packages=['cli_anything.alloy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-alloy=cli_anything.alloy:cli']},
)
