from setuptools import setup
setup(
    name='cli-anything-opnsense',
    version='1.0.0',
    packages=['cli_anything.opnsense'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-opnsense=cli_anything.opnsense:cli']},
)
