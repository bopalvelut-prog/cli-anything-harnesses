from setuptools import setup
setup(
    name='cli-anything-descheduler',
    version='1.0.0',
    packages=['cli_anything.descheduler'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-descheduler=cli_anything.descheduler:cli']},
)
