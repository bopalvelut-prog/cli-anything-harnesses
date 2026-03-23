from setuptools import setup
setup(
    name='cli-anything-subsystem_v2',
    version='1.0.0',
    packages=['cli_anything.subsystem_v2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-subsystem_v2=cli_anything.subsystem_v2:cli']},
)
