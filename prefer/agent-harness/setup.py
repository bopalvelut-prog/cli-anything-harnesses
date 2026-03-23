from setuptools import setup
setup(
    name='cli-anything-prefer',
    version='1.0.0',
    packages=['cli_anything.prefer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prefer=cli_anything.prefer:cli']},
)
