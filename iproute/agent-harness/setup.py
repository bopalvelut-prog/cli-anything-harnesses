from setuptools import setup
setup(
    name='cli-anything-iproute',
    version='1.0.0',
    packages=['cli_anything.iproute'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-iproute=cli_anything.iproute:cli']},
)
