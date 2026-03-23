from setuptools import setup
setup(
    name='cli-anything-monitor',
    version='1.0.0',
    packages=['cli_anything.monitor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-monitor=cli_anything.monitor:cli']},
)
