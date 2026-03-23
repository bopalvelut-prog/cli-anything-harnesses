from setuptools import setup
setup(
    name='cli-anything-bmc',
    version='1.0.0',
    packages=['cli_anything.bmc'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bmc=cli_anything.bmc:cli']},
)
