from setuptools import setup
setup(
    name='cli-anything-gcp_memorystore',
    version='1.0.0',
    packages=['cli_anything.gcp_memorystore'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gcp_memorystore=cli_anything.gcp_memorystore:cli']},
)
