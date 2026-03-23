from setuptools import setup
setup(
    name='cli-anything-pitest',
    version='1.0.0',
    packages=['cli_anything.pitest'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pitest=cli_anything.pitest:cli']},
)
