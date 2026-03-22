from setuptools import setup
setup(
    name='cli-anything-backblaze',
    version='1.0.0',
    packages=['cli_anything.backblaze'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-backblaze=cli_anything.backblaze:cli']},
)
