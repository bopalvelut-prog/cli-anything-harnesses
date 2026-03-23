from setuptools import setup
setup(
    name='cli-anything-eucalyptus',
    version='1.0.0',
    packages=['cli_anything.eucalyptus'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-eucalyptus=cli_anything.eucalyptus:cli']},
)
