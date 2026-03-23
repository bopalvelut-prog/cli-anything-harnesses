from setuptools import setup
setup(
    name='cli-anything-alluxio',
    version='1.0.0',
    packages=['cli_anything.alluxio'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-alluxio=cli_anything.alluxio:cli']},
)
