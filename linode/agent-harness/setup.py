from setuptools import setup
setup(
    name='cli-anything-linode',
    version='1.0.0',
    packages=['cli_anything.linode'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-linode=cli_anything.linode:cli']},
)
