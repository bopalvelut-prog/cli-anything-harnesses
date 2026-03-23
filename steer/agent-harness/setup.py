from setuptools import setup
setup(
    name='cli-anything-steer',
    version='1.0.0',
    packages=['cli_anything.steer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-steer=cli_anything.steer:cli']},
)
