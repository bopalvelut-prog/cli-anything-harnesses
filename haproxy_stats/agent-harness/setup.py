from setuptools import setup
setup(
    name='cli-anything-haproxy_stats',
    version='1.0.0',
    packages=['cli_anything.haproxy_stats'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-haproxy_stats=cli_anything.haproxy_stats:cli']},
)
