from setuptools import setup
setup(
    name='cli-anything-nfs',
    version='1.0.0',
    packages=['cli_anything.nfs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nfs=cli_anything.nfs:cli']},
)
