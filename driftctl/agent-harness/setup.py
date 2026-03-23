from setuptools import setup
setup(
    name='cli-anything-driftctl',
    version='1.0.0',
    packages=['cli_anything.driftctl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-driftctl=cli_anything.driftctl:cli']},
)
