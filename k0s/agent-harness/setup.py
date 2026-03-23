from setuptools import setup
setup(
    name='cli-anything-k0s',
    version='1.0.0',
    packages=['cli_anything.k0s'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-k0s=cli_anything.k0s:cli']},
)
