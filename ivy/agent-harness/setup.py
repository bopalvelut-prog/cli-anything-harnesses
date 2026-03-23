from setuptools import setup
setup(
    name='cli-anything-ivy',
    version='1.0.0',
    packages=['cli_anything.ivy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ivy=cli_anything.ivy:cli']},
)
