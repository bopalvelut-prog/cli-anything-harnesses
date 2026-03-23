from setuptools import setup
setup(
    name='cli-anything-netdata',
    version='1.0.0',
    packages=['cli_anything.netdata'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-netdata=cli_anything.netdata:cli']},
)
