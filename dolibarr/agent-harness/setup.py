from setuptools import setup
setup(
    name='cli-anything-dolibarr',
    version='1.0.0',
    packages=['cli_anything.dolibarr'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dolibarr=cli_anything.dolibarr:cli']},
)
