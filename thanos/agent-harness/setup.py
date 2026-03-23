from setuptools import setup
setup(
    name='cli-anything-thanos',
    version='1.0.0',
    packages=['cli_anything.thanos'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-thanos=cli_anything.thanos:cli']},
)
