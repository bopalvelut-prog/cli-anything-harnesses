from setuptools import setup
setup(
    name='cli-anything-configmap',
    version='1.0.0',
    packages=['cli_anything.configmap'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-configmap=cli_anything.configmap:cli']},
)
