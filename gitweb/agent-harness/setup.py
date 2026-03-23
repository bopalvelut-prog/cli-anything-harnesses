from setuptools import setup
setup(
    name='cli-anything-gitweb',
    version='1.0.0',
    packages=['cli_anything.gitweb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gitweb=cli_anything.gitweb:cli']},
)
