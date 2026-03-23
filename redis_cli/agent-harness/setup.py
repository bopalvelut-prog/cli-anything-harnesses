from setuptools import setup
setup(
    name='cli-anything-redis_cli',
    version='1.0.0',
    packages=['cli_anything.redis_cli'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-redis_cli=cli_anything.redis_cli:cli']},
)
