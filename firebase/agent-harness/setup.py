from setuptools import setup
setup(
    name='cli-anything-firebase',
    version='1.0.0',
    packages=['cli_anything.firebase'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-firebase=cli_anything.firebase:cli']},
)
