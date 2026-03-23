from setuptools import setup
setup(
    name='cli-anything-puppetserver',
    version='1.0.0',
    packages=['cli_anything.puppetserver'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-puppetserver=cli_anything.puppetserver:cli']},
)
