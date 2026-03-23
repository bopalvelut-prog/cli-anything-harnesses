from setuptools import setup
setup(
    name='cli-anything-cloudify',
    version='1.0.0',
    packages=['cli_anything.cloudify'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cloudify=cli_anything.cloudify:cli']},
)
