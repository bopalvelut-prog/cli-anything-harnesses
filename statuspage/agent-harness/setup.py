from setuptools import setup
setup(
    name='cli-anything-statuspage',
    version='1.0.0',
    packages=['cli_anything.statuspage'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-statuspage=cli_anything.statuspage:cli']},
)
