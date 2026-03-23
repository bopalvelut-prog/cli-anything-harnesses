from setuptools import setup
setup(
    name='cli-anything-centerim',
    version='1.0.0',
    packages=['cli_anything.centerim'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-centerim=cli_anything.centerim:cli']},
)
