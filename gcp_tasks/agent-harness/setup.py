from setuptools import setup
setup(
    name='cli-anything-gcp_tasks',
    version='1.0.0',
    packages=['cli_anything.gcp_tasks'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gcp_tasks=cli_anything.gcp_tasks:cli']},
)
