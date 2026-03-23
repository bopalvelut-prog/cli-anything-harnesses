from setuptools import setup
setup(
    name='cli-anything-buildah',
    version='1.0.0',
    packages=['cli_anything.buildah'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-buildah=cli_anything.buildah:cli']},
)
