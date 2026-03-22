from setuptools import setup
setup(
    name='cli-anything-sysdig',
    version='1.0.0',
    packages=['cli_anything.sysdig'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sysdig=cli_anything.sysdig:cli']},
)
