from setuptools import setup
setup(
    name='cli-anything-thin_v2',
    version='1.0.0',
    packages=['cli_anything.thin_v2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-thin_v2=cli_anything.thin_v2:cli']},
)
