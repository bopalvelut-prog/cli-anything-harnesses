from setuptools import setup
setup(
    name='cli-anything-nexus',
    version='1.0.0',
    packages=['cli_anything.nexus'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nexus=cli_anything.nexus:cli']},
)
