from setuptools import setup
setup(
    name='cli-anything-rke2',
    version='1.0.0',
    packages=['cli_anything.rke2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rke2=cli_anything.rke2:cli']},
)
