from setuptools import setup
setup(
    name='cli-anything-popeye',
    version='1.0.0',
    packages=['cli_anything.popeye'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-popeye=cli_anything.popeye:cli']},
)
