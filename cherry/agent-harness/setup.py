from setuptools import setup
setup(
    name='cli-anything-cherry',
    version='1.0.0',
    packages=['cli_anything.cherry'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cherry=cli_anything.cherry:cli']},
)
