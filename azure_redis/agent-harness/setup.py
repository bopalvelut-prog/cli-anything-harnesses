from setuptools import setup
setup(
    name='cli-anything-azure_redis',
    version='1.0.0',
    packages=['cli_anything.azure_redis'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-azure_redis=cli_anything.azure_redis:cli']},
)
