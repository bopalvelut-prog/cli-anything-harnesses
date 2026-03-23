from setuptools import setup
setup(
    name='cli-anything-varnish',
    version='1.0.0',
    packages=['cli_anything.varnish'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-varnish=cli_anything.varnish:cli']},
)
