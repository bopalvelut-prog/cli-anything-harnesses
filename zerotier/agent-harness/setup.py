from setuptools import setup
setup(
    name='cli-anything-zerotier',
    version='1.0.0',
    packages=['cli_anything.zerotier'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zerotier=cli_anything.zerotier:cli']},
)
