from setuptools import setup
setup(
    name='cli-anything-kickstart',
    version='1.0.0',
    packages=['cli_anything.kickstart'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kickstart=cli_anything.kickstart:cli']},
)
