from setuptools import setup
setup(
    name='cli-anything-naiveproxy',
    version='1.0.0',
    packages=['cli_anything.naiveproxy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-naiveproxy=cli_anything.naiveproxy:cli']},
)
