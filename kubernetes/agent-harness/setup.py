from setuptools import setup
setup(
    name='cli-anything-kubernetes',
    version='1.0.0',
    packages=['cli_anything.kubernetes'],
    install_requires=['click', 'kubernetes'],
    entry_points={'console_scripts': ['cli-anything-kubernetes=cli_anything.kubernetes:cli']},
)
