from setuptools import setup
setup(
    name='cli-anything-mfaserver',
    version='1.0.0',
    packages=['cli_anything.mfaserver'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mfaserver=cli_anything.mfaserver:cli']},
)
