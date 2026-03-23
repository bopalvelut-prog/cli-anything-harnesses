from setuptools import setup
setup(
    name='cli-anything-misp',
    version='1.0.0',
    packages=['cli_anything.misp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-misp=cli_anything.misp:cli']},
)
