from setuptools import setup
setup(
    name='cli-anything-aws',
    version='1.0.0',
    packages=['cli_anything.aws'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aws=cli_anything.aws:cli']},
)
