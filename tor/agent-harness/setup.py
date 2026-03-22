from setuptools import setup
setup(
    name='cli-anything-tor',
    version='1.0.0',
    packages=['cli_anything.tor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tor=cli_anything.tor:cli']},
)
