from setuptools import setup
setup(
    name='cli-anything-argus',
    version='1.0.0',
    packages=['cli_anything.argus'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-argus=cli_anything.argus:cli']},
)
