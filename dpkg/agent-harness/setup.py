from setuptools import setup
setup(
    name='cli-anything-dpkg',
    version='1.0.0',
    packages=['cli_anything.dpkg'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dpkg=cli_anything.dpkg:cli']},
)
