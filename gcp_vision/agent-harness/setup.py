from setuptools import setup
setup(
    name='cli-anything-gcp_vision',
    version='1.0.0',
    packages=['cli_anything.gcp_vision'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gcp_vision=cli_anything.gcp_vision:cli']},
)
