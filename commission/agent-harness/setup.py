from setuptools import setup
setup(
    name='cli-anything-commission',
    version='1.0.0',
    packages=['cli_anything.commission'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-commission=cli_anything.commission:cli']},
)
