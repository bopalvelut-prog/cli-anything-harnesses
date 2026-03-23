from setuptools import setup
setup(
    name='cli-anything-vessel',
    version='1.0.0',
    packages=['cli_anything.vessel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vessel=cli_anything.vessel:cli']},
)
