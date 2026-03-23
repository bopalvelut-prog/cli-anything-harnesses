from setuptools import setup
setup(
    name='cli-anything-kubesphere',
    version='1.0.0',
    packages=['cli_anything.kubesphere'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kubesphere=cli_anything.kubesphere:cli']},
)
