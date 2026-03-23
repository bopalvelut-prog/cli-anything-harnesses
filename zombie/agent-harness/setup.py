from setuptools import setup
setup(
    name='cli-anything-zombie',
    version='1.0.0',
    packages=['cli_anything.zombie'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zombie=cli_anything.zombie:cli']},
)
