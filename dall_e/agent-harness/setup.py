from setuptools import setup
setup(
    name='cli-anything-dall_e',
    version='1.0.0',
    packages=['cli_anything.dall_e'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dall_e=cli_anything.dall_e:cli']},
)
