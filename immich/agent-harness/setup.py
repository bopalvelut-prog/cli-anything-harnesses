from setuptools import setup
setup(
    name='cli-anything-immich',
    version='1.0.0',
    packages=['cli_anything.immich'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-immich=cli_anything.immich:cli']},
)
