from setuptools import setup
setup(
    name='cli-anything-ankr',
    version='1.0.0',
    packages=['cli_anything.ankr'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ankr=cli_anything.ankr:cli']},
)
