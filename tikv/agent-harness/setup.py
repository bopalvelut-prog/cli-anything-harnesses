from setuptools import setup
setup(
    name='cli-anything-tikv',
    version='1.0.0',
    packages=['cli_anything.tikv'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tikv=cli_anything.tikv:cli']},
)
