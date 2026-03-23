from setuptools import setup
setup(
    name='cli-anything-till_v2',
    version='1.0.0',
    packages=['cli_anything.till_v2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-till_v2=cli_anything.till_v2:cli']},
)
