from setuptools import setup
setup(
    name='cli-anything-scheduler',
    version='1.0.0',
    packages=['cli_anything.scheduler'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scheduler=cli_anything.scheduler:cli']},
)
