from setuptools import setup
setup(
    name='cli-anything-restriction',
    version='1.0.0',
    packages=['cli_anything.restriction'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-restriction=cli_anything.restriction:cli']},
)
