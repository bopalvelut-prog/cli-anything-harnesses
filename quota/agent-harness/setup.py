from setuptools import setup
setup(
    name='cli-anything-quota',
    version='1.0.0',
    packages=['cli_anything.quota'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-quota=cli_anything.quota:cli']},
)
