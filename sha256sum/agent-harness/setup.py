from setuptools import setup
setup(
    name='cli-anything-sha256sum',
    version='1.0.0',
    packages=['cli_anything.sha256sum'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sha256sum=cli_anything.sha256sum:cli']},
)
