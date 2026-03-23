from setuptools import setup
setup(
    name='cli-anything-hetzner_cloud',
    version='1.0.0',
    packages=['cli_anything.hetzner_cloud'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hetzner_cloud=cli_anything.hetzner_cloud:cli']},
)
