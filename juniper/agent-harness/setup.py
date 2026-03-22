from setuptools import setup
setup(
    name='cli-anything-juniper',
    version='1.0.0',
    packages=['cli_anything.juniper'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-juniper=cli_anything.juniper:cli']},
)
