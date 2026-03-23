from setuptools import setup
setup(
    name='cli-anything-nutanix',
    version='1.0.0',
    packages=['cli_anything.nutanix'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nutanix=cli_anything.nutanix:cli']},
)
