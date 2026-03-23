from setuptools import setup
setup(
    name='cli-anything-widely',
    version='1.0.0',
    packages=['cli_anything.widely'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-widely=cli_anything.widely:cli']},
)
