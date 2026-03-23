from setuptools import setup
setup(
    name='cli-anything-gcp_pubsub',
    version='1.0.0',
    packages=['cli_anything.gcp_pubsub'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gcp_pubsub=cli_anything.gcp_pubsub:cli']},
)
