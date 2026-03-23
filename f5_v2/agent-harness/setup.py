from setuptools import setup
setup(
    name='cli-anything-f5_v2',
    version='1.0.0',
    packages=['cli_anything.f5_v2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-f5_v2=cli_anything.f5_v2:cli']},
)
