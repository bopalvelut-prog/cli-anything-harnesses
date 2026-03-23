from setuptools import setup
setup(
    name='cli-anything-proxy',
    version='1.0.0',
    packages=['cli_anything.proxy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-proxy=cli_anything.proxy:cli']},
)
