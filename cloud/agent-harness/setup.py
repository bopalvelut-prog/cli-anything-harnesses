from setuptools import setup
setup(
    name='cli-anything-cloud',
    version='1.0.0',
    packages=['cli_anything.cloud'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cloud=cli_anything.cloud:cli']},
)
