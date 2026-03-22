from setuptools import setup
setup(
    name='cli-anything-terra_2',
    version='1.0.0',
    packages=['cli_anything.terra_2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-terra_2=cli_anything.terra_2:cli']},
)
