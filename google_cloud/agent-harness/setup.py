from setuptools import setup
setup(
    name='cli-anything-google_cloud',
    version='1.0.0',
    packages=['cli_anything.google_cloud'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-google_cloud=cli_anything.google_cloud:cli']},
)
