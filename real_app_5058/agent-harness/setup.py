from setuptools import setup
setup(
    name='cli-anything-real_app_5058',
    version='1.0.0',
    packages=['cli_anything.real_app_5058'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-real_app_5058=cli_anything.real_app_5058:cli']},
)
