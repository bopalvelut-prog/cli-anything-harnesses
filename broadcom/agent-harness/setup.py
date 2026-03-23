from setuptools import setup
setup(
    name='cli-anything-broadcom',
    version='1.0.0',
    packages=['cli_anything.broadcom'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-broadcom=cli_anything.broadcom:cli']},
)
