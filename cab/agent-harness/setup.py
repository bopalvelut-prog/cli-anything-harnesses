from setuptools import setup
setup(
    name='cli-anything-cab',
    version='1.0.0',
    packages=['cli_anything.cab'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cab=cli_anything.cab:cli']},
)
