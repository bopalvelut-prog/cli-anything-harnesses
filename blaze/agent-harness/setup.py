from setuptools import setup
setup(
    name='cli-anything-blaze',
    version='1.0.0',
    packages=['cli_anything.blaze'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-blaze=cli_anything.blaze:cli']},
)
