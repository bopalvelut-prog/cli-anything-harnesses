from setuptools import setup
setup(
    name='cli-anything-recovery',
    version='1.0.0',
    packages=['cli_anything.recovery'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-recovery=cli_anything.recovery:cli']},
)
