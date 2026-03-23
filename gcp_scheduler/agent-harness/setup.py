from setuptools import setup
setup(
    name='cli-anything-gcp_scheduler',
    version='1.0.0',
    packages=['cli_anything.gcp_scheduler'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gcp_scheduler=cli_anything.gcp_scheduler:cli']},
)
