from setuptools import setup
setup(
    name='cli-anything-switch',
    version='1.0.0',
    packages=['cli_anything.switch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-switch=cli_anything.switch:cli']},
)
