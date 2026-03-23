from setuptools import setup
setup(
    name='cli-anything-foot',
    version='1.0.0',
    packages=['cli_anything.foot'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-foot=cli_anything.foot:cli']},
)
