from setuptools import setup
setup(
    name='cli-anything-gcp_storage',
    version='1.0.0',
    packages=['cli_anything.gcp_storage'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gcp_storage=cli_anything.gcp_storage:cli']},
)
