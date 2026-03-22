from setuptools import setup
setup(
    name='cli-anything-redis_admin',
    version='1.0.0',
    packages=['cli_anything.redis_admin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-redis_admin=cli_anything.redis_admin:cli']},
)
