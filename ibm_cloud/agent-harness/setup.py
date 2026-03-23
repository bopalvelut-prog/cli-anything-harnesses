from setuptools import setup
setup(
    name='cli-anything-ibm_cloud',
    version='1.0.0',
    packages=['cli_anything.ibm_cloud'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ibm_cloud=cli_anything.ibm_cloud:cli']},
)
