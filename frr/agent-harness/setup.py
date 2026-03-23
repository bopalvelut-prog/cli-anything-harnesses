from setuptools import setup
setup(
    name='cli-anything-frr',
    version='1.0.0',
    packages=['cli_anything.frr'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-frr=cli_anything.frr:cli']},
)
