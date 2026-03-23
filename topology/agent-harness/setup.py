from setuptools import setup
setup(
    name='cli-anything-topology',
    version='1.0.0',
    packages=['cli_anything.topology'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-topology=cli_anything.topology:cli']},
)
