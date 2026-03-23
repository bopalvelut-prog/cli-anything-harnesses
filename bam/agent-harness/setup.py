from setuptools import setup
setup(
    name='cli-anything-bam',
    version='1.0.0',
    packages=['cli_anything.bam'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bam=cli_anything.bam:cli']},
)
