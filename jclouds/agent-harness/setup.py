from setuptools import setup
setup(
    name='cli-anything-jclouds',
    version='1.0.0',
    packages=['cli_anything.jclouds'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jclouds=cli_anything.jclouds:cli']},
)
