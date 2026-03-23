from setuptools import setup
setup(
    name='cli-anything-appcenter',
    version='1.0.0',
    packages=['cli_anything.appcenter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-appcenter=cli_anything.appcenter:cli']},
)
