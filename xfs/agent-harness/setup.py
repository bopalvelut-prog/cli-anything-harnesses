from setuptools import setup
setup(
    name='cli-anything-xfs',
    version='1.0.0',
    packages=['cli_anything.xfs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-xfs=cli_anything.xfs:cli']},
)
