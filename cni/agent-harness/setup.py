from setuptools import setup
setup(
    name='cli-anything-cni',
    version='1.0.0',
    packages=['cli_anything.cni'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cni=cli_anything.cni:cli']},
)
