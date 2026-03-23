from setuptools import setup
setup(
    name='cli-anything-sota',
    version='1.0.0',
    packages=['cli_anything.sota'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sota=cli_anything.sota:cli']},
)
