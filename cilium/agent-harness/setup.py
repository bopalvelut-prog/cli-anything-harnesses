from setuptools import setup
setup(
    name='cli-anything-cilium',
    version='1.0.0',
    packages=['cli_anything.cilium'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cilium=cli_anything.cilium:cli']},
)
