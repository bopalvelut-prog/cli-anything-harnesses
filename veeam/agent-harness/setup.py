from setuptools import setup
setup(
    name='cli-anything-veeam',
    version='1.0.0',
    packages=['cli_anything.veeam'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-veeam=cli_anything.veeam:cli']},
)
