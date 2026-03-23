from setuptools import setup
setup(
    name='cli-anything-oci',
    version='1.0.0',
    packages=['cli_anything.oci'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-oci=cli_anything.oci:cli']},
)
