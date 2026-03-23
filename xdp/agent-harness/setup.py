from setuptools import setup
setup(
    name='cli-anything-xdp',
    version='1.0.0',
    packages=['cli_anything.xdp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-xdp=cli_anything.xdp:cli']},
)
