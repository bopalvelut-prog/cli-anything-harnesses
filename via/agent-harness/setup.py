from setuptools import setup
setup(
    name='cli-anything-via',
    version='1.0.0',
    packages=['cli_anything.via'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-via=cli_anything.via:cli']},
)
