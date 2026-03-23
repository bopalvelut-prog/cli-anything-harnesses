from setuptools import setup
setup(
    name='cli-anything-gitpod',
    version='1.0.0',
    packages=['cli_anything.gitpod'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gitpod=cli_anything.gitpod:cli']},
)
