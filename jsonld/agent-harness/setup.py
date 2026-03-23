from setuptools import setup
setup(
    name='cli-anything-jsonld',
    version='1.0.0',
    packages=['cli_anything.jsonld'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jsonld=cli_anything.jsonld:cli']},
)
