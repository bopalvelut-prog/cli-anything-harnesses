from setuptools import setup
setup(
    name='cli-anything-member',
    version='1.0.0',
    packages=['cli_anything.member'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-member=cli_anything.member:cli']},
)
