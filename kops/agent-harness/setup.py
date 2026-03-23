from setuptools import setup
setup(
    name='cli-anything-kops',
    version='1.0.0',
    packages=['cli_anything.kops'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kops=cli_anything.kops:cli']},
)
