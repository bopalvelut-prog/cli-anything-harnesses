from setuptools import setup
setup(
    name='cli-anything-workload',
    version='1.0.0',
    packages=['cli_anything.workload'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-workload=cli_anything.workload:cli']},
)
