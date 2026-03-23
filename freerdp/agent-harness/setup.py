from setuptools import setup
setup(
    name='cli-anything-freerdp',
    version='1.0.0',
    packages=['cli_anything.freerdp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-freerdp=cli_anything.freerdp:cli']},
)
