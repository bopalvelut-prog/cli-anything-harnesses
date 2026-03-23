from setuptools import setup
setup(
    name='cli-anything-redis_cluster',
    version='1.0.0',
    packages=['cli_anything.redis_cluster'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-redis_cluster=cli_anything.redis_cluster:cli']},
)
