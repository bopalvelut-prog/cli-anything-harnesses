from setuptools import setup
setup(
    name='cli-anything-siemens',
    version='1.0.0',
    packages=['cli_anything.siemens'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-siemens=cli_anything.siemens:cli']},
)
