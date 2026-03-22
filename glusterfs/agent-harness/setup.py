from setuptools import setup
setup(
    name='cli-anything-glusterfs',
    version='1.0.0',
    packages=['cli_anything.glusterfs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-glusterfs=cli_anything.glusterfs:cli']},
)
