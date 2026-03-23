from setuptools import setup
setup(
    name='cli-anything-shock',
    version='1.0.0',
    packages=['cli_anything.shock'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shock=cli_anything.shock:cli']},
)
