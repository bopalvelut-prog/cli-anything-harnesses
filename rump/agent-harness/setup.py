from setuptools import setup
setup(
    name='cli-anything-rump',
    version='1.0.0',
    packages=['cli_anything.rump'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rump=cli_anything.rump:cli']},
)
