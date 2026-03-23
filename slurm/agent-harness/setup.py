from setuptools import setup
setup(
    name='cli-anything-slurm',
    version='1.0.0',
    packages=['cli_anything.slurm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-slurm=cli_anything.slurm:cli']},
)
