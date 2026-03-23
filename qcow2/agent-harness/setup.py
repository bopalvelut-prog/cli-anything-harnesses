from setuptools import setup
setup(
    name='cli-anything-qcow2',
    version='1.0.0',
    packages=['cli_anything.qcow2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-qcow2=cli_anything.qcow2:cli']},
)
