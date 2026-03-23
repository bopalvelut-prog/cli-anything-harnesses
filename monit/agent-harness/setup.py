from setuptools import setup
setup(
    name='cli-anything-monit',
    version='1.0.0',
    packages=['cli_anything.monit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-monit=cli_anything.monit:cli']},
)
