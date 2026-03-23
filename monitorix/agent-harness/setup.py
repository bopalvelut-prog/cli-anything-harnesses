from setuptools import setup
setup(
    name='cli-anything-monitorix',
    version='1.0.0',
    packages=['cli_anything.monitorix'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-monitorix=cli_anything.monitorix:cli']},
)
