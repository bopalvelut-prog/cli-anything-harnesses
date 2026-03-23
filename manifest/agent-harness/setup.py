from setuptools import setup
setup(
    name='cli-anything-manifest',
    version='1.0.0',
    packages=['cli_anything.manifest'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-manifest=cli_anything.manifest:cli']},
)
