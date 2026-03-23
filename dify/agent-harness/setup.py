from setuptools import setup
setup(
    name='cli-anything-dify',
    version='1.0.0',
    packages=['cli_anything.dify'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dify=cli_anything.dify:cli']},
)
