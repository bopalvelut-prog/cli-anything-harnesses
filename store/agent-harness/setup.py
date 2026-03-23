from setuptools import setup
setup(
    name='cli-anything-store',
    version='1.0.0',
    packages=['cli_anything.store'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-store=cli_anything.store:cli']},
)
