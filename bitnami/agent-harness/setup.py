from setuptools import setup
setup(
    name='cli-anything-bitnami',
    version='1.0.0',
    packages=['cli_anything.bitnami'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bitnami=cli_anything.bitnami:cli']},
)
