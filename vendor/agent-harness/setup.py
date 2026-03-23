from setuptools import setup
setup(
    name='cli-anything-vendor',
    version='1.0.0',
    packages=['cli_anything.vendor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vendor=cli_anything.vendor:cli']},
)
