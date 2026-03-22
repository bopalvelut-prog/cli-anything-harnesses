from setuptools import setup
setup(
    name='cli-anything-redis',
    version='1.0.0',
    packages=['cli_anything.redis'],
    install_requires=['click', 'redis'],
    entry_points={'console_scripts': ['cli-anything-redis=cli_anything.redis:cli']},
)
