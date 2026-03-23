from setuptools import setup
setup(
    name='cli-anything-zypper',
    version='1.0.0',
    packages=['cli_anything.zypper'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zypper=cli_anything.zypper:cli']},
)
