from setuptools import setup
setup(
    name='cli-anything-limactl',
    version='1.0.0',
    packages=['cli_anything.limactl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-limactl=cli_anything.limactl:cli']},
)
