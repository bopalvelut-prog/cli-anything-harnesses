from setuptools import setup
setup(
    name='cli-anything-agora',
    version='1.0.0',
    packages=['cli_anything.agora'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-agora=cli_anything.agora:cli']},
)
