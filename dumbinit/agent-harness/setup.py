from setuptools import setup
setup(
    name='cli-anything-dumbinit',
    version='1.0.0',
    packages=['cli_anything.dumbinit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dumbinit=cli_anything.dumbinit:cli']},
)
