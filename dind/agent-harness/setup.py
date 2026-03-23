from setuptools import setup
setup(
    name='cli-anything-dind',
    version='1.0.0',
    packages=['cli_anything.dind'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dind=cli_anything.dind:cli']},
)
