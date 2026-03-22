from setuptools import setup
setup(
    name='cli-anything-metamask',
    version='1.0.0',
    packages=['cli_anything.metamask'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-metamask=cli_anything.metamask:cli']},
)
