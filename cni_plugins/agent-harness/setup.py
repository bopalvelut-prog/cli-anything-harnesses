from setuptools import setup
setup(
    name='cli-anything-cni_plugins',
    version='1.0.0',
    packages=['cli_anything.cni_plugins'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cni_plugins=cli_anything.cni_plugins:cli']},
)
