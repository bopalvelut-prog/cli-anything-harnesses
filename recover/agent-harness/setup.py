from setuptools import setup
setup(
    name='cli-anything-recover',
    version='1.0.0',
    packages=['cli_anything.recover'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-recover=cli_anything.recover:cli']},
)
