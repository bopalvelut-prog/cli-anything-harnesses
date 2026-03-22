from setuptools import setup
setup(
    name='cli-anything-rancher',
    version='1.0.0',
    packages=['cli_anything.rancher'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rancher=cli_anything.rancher:cli']},
)
