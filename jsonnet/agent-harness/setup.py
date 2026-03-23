from setuptools import setup
setup(
    name='cli-anything-jsonnet',
    version='1.0.0',
    packages=['cli_anything.jsonnet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jsonnet=cli_anything.jsonnet:cli']},
)
