from setuptools import setup
setup(
    name='cli-anything-midgard',
    version='1.0.0',
    packages=['cli_anything.midgard'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-midgard=cli_anything.midgard:cli']},
)
