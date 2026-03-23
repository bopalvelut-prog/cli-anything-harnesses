from setuptools import setup
setup(
    name='cli-anything-nacos',
    version='1.0.0',
    packages=['cli_anything.nacos'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nacos=cli_anything.nacos:cli']},
)
