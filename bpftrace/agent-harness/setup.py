from setuptools import setup
setup(
    name='cli-anything-bpftrace',
    version='1.0.0',
    packages=['cli_anything.bpftrace'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bpftrace=cli_anything.bpftrace:cli']},
)
