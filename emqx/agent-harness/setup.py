from setuptools import setup
setup(
    name='cli-anything-emqx',
    version='1.0.0',
    packages=['cli_anything.emqx'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-emqx=cli_anything.emqx:cli']},
)
