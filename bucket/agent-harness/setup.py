from setuptools import setup
setup(
    name='cli-anything-bucket',
    version='1.0.0',
    packages=['cli_anything.bucket'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bucket=cli_anything.bucket:cli']},
)
