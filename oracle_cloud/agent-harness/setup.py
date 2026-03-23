from setuptools import setup
setup(
    name='cli-anything-oracle_cloud',
    version='1.0.0',
    packages=['cli_anything.oracle_cloud'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-oracle_cloud=cli_anything.oracle_cloud:cli']},
)
