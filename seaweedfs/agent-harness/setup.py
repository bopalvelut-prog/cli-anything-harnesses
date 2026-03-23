from setuptools import setup
setup(
    name='cli-anything-seaweedfs',
    version='1.0.0',
    packages=['cli_anything.seaweedfs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-seaweedfs=cli_anything.seaweedfs:cli']},
)
