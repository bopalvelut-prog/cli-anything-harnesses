from setuptools import setup
setup(
    name='cli-anything-prowlarr',
    version='1.0.0',
    packages=['cli_anything.prowlarr'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prowlarr=cli_anything.prowlarr:cli']},
)
