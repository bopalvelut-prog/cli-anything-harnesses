from setuptools import setup
setup(
    name='cli-anything-google_keep',
    version='1.0.0',
    packages=['cli_anything.google_keep'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-google_keep=cli_anything.google_keep:cli']},
)
