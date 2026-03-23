from setuptools import setup
setup(
    name='cli-anything-netfilter',
    version='1.0.0',
    packages=['cli_anything.netfilter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-netfilter=cli_anything.netfilter:cli']},
)
