from setuptools import setup
setup(
    name='cli-anything-mtu',
    version='1.0.0',
    packages=['cli_anything.mtu'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mtu=cli_anything.mtu:cli']},
)
