from setuptools import setup
setup(
    name='cli-anything-redis_sentinel',
    version='1.0.0',
    packages=['cli_anything.redis_sentinel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-redis_sentinel=cli_anything.redis_sentinel:cli']},
)
