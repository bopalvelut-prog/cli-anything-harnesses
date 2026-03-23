from setuptools import setup
setup(
    name='cli-anything-puppetdb',
    version='1.0.0',
    packages=['cli_anything.puppetdb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-puppetdb=cli_anything.puppetdb:cli']},
)
