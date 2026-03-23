from setuptools import setup
setup(
    name='cli-anything-gotty',
    version='1.0.0',
    packages=['cli_anything.gotty'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gotty=cli_anything.gotty:cli']},
)
