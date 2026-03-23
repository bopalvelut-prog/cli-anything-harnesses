from setuptools import setup
setup(
    name='cli-anything-adobe_xd',
    version='1.0.0',
    packages=['cli_anything.adobe_xd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-adobe_xd=cli_anything.adobe_xd:cli']},
)
