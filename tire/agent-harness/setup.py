from setuptools import setup
setup(
    name='cli-anything-tire',
    version='1.0.0',
    packages=['cli_anything.tire'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tire=cli_anything.tire:cli']},
)
