from setuptools import setup
setup(
    name='cli-anything-extra',
    version='1.0.0',
    packages=['cli_anything.extra'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-extra=cli_anything.extra:cli']},
)
