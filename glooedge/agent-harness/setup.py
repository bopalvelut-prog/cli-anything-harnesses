from setuptools import setup
setup(
    name='cli-anything-glooedge',
    version='1.0.0',
    packages=['cli_anything.glooedge'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-glooedge=cli_anything.glooedge:cli']},
)
