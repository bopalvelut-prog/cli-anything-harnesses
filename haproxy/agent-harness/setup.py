from setuptools import setup
setup(
    name='cli-anything-haproxy',
    version='1.0.0',
    packages=['cli_anything.haproxy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-haproxy=cli_anything.haproxy:cli']},
)
