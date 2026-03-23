from setuptools import setup
setup(
    name='cli-anything-gcp_redis',
    version='1.0.0',
    packages=['cli_anything.gcp_redis'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gcp_redis=cli_anything.gcp_redis:cli']},
)
