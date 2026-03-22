from setuptools import setup
setup(
    name='cli-anything-photoprism',
    version='1.0.0',
    packages=['cli_anything.photoprism'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-photoprism=cli_anything.photoprism:cli']},
)
