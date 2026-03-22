from setuptools import setup
setup(
    name='cli-anything-memcached',
    version='1.0.0',
    packages=['cli_anything.memcached'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-memcached=cli_anything.memcached:cli']},
)
