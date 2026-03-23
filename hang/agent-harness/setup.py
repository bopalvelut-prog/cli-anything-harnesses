from setuptools import setup
setup(
    name='cli-anything-hang',
    version='1.0.0',
    packages=['cli_anything.hang'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hang=cli_anything.hang:cli']},
)
