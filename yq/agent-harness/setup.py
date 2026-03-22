from setuptools import setup
setup(
    name='cli-anything-yq',
    version='1.0.0',
    packages=['cli_anything.yq'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-yq=cli_anything.yq:cli']},
)
