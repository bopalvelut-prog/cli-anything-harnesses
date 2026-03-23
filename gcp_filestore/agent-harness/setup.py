from setuptools import setup
setup(
    name='cli-anything-gcp_filestore',
    version='1.0.0',
    packages=['cli_anything.gcp_filestore'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gcp_filestore=cli_anything.gcp_filestore:cli']},
)
