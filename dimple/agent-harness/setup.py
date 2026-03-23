from setuptools import setup
setup(
    name='cli-anything-dimple',
    version='1.0.0',
    packages=['cli_anything.dimple'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dimple=cli_anything.dimple:cli']},
)
