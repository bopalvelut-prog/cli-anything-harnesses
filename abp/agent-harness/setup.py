from setuptools import setup
setup(
    name='cli-anything-abp',
    version='1.0.0',
    packages=['cli_anything.abp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-abp=cli_anything.abp:cli']},
)
