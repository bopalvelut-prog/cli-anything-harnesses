from setuptools import setup
setup(
    name='cli-anything-uptime',
    version='1.0.0',
    packages=['cli_anything.uptime'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-uptime=cli_anything.uptime:cli']},
)
