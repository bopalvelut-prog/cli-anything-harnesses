from setuptools import setup
setup(
    name='cli-anything-arp',
    version='1.0.0',
    packages=['cli_anything.arp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-arp=cli_anything.arp:cli']},
)
