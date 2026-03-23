from setuptools import setup
setup(
    name='cli-anything-disc',
    version='1.0.0',
    packages=['cli_anything.disc'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-disc=cli_anything.disc:cli']},
)
