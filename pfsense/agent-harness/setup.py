from setuptools import setup
setup(
    name='cli-anything-pfsense',
    version='1.0.0',
    packages=['cli_anything.pfsense'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pfsense=cli_anything.pfsense:cli']},
)
