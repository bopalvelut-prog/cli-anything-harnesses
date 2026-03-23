from setuptools import setup
setup(
    name='cli-anything-general',
    version='1.0.0',
    packages=['cli_anything.general'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-general=cli_anything.general:cli']},
)
