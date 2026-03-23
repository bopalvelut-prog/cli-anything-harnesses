from setuptools import setup
setup(
    name='cli-anything-deepvariant',
    version='1.0.0',
    packages=['cli_anything.deepvariant'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-deepvariant=cli_anything.deepvariant:cli']},
)
