from setuptools import setup
setup(
    name='cli-anything-appwrite',
    version='1.0.0',
    packages=['cli_anything.appwrite'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-appwrite=cli_anything.appwrite:cli']},
)
