from setuptools import setup
setup(
    name='cli-anything-sysstat',
    version='1.0.0',
    packages=['cli_anything.sysstat'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sysstat=cli_anything.sysstat:cli']},
)
