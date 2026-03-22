from setuptools import setup
setup(
    name='cli-anything-intercom',
    version='1.0.0',
    packages=['cli_anything.intercom'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-intercom=cli_anything.intercom:cli']},
)
