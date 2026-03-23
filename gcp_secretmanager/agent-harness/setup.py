from setuptools import setup
setup(
    name='cli-anything-gcp_secretmanager',
    version='1.0.0',
    packages=['cli_anything.gcp_secretmanager'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gcp_secretmanager=cli_anything.gcp_secretmanager:cli']},
)
