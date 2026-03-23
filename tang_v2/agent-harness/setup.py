from setuptools import setup
setup(
    name='cli-anything-tang_v2',
    version='1.0.0',
    packages=['cli_anything.tang_v2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tang_v2=cli_anything.tang_v2:cli']},
)
