from setuptools import setup
setup(
    name='cli-anything-openresty',
    version='1.0.0',
    packages=['cli_anything.openresty'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-openresty=cli_anything.openresty:cli']},
)
