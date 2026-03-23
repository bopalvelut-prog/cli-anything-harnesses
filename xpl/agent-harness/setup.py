from setuptools import setup
setup(
    name='cli-anything-xpl',
    version='1.0.0',
    packages=['cli_anything.xpl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-xpl=cli_anything.xpl:cli']},
)
