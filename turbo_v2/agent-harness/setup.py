from setuptools import setup
setup(
    name='cli-anything-turbo_v2',
    version='1.0.0',
    packages=['cli_anything.turbo_v2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-turbo_v2=cli_anything.turbo_v2:cli']},
)
