from setuptools import setup
setup(
    name='cli-anything-gcp_workflows',
    version='1.0.0',
    packages=['cli_anything.gcp_workflows'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gcp_workflows=cli_anything.gcp_workflows:cli']},
)
