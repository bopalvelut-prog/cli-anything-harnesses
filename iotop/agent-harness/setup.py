from setuptools import setup
setup(
    name='cli-anything-iotop',
    version='1.0.0',
    packages=['cli_anything.iotop'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-iotop=cli_anything.iotop:cli']},
)
