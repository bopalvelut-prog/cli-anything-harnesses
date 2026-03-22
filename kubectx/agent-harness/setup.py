from setuptools import setup
setup(
    name='cli-anything-kubectx',
    version='1.0.0',
    packages=['cli_anything.kubectx'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kubectx=cli_anything.kubectx:cli']},
)
