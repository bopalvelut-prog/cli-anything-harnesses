from setuptools import setup
setup(
    name='cli-anything-xyz',
    version='1.0.0',
    packages=['cli_anything.xyz'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-xyz=cli_anything.xyz:cli']},
)
