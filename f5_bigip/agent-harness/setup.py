from setuptools import setup
setup(
    name='cli-anything-f5_bigip',
    version='1.0.0',
    packages=['cli_anything.f5_bigip'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-f5_bigip=cli_anything.f5_bigip:cli']},
)
