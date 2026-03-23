from setuptools import setup
setup(
    name='cli-anything-modsecurity',
    version='1.0.0',
    packages=['cli_anything.modsecurity'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-modsecurity=cli_anything.modsecurity:cli']},
)
