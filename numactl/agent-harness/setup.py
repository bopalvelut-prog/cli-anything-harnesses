from setuptools import setup
setup(
    name='cli-anything-numactl',
    version='1.0.0',
    packages=['cli_anything.numactl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-numactl=cli_anything.numactl:cli']},
)
