from setuptools import setup
setup(
    name='cli-anything-rendezvous',
    version='1.0.0',
    packages=['cli_anything.rendezvous'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rendezvous=cli_anything.rendezvous:cli']},
)
