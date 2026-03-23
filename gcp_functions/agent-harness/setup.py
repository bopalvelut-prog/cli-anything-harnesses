from setuptools import setup
setup(
    name='cli-anything-gcp_functions',
    version='1.0.0',
    packages=['cli_anything.gcp_functions'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gcp_functions=cli_anything.gcp_functions:cli']},
)
