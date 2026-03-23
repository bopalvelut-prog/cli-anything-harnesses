from setuptools import setup
setup(
    name='cli-anything-coturn',
    version='1.0.0',
    packages=['cli_anything.coturn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-coturn=cli_anything.coturn:cli']},
)
