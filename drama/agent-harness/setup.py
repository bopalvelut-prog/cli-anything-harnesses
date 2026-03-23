from setuptools import setup
setup(
    name='cli-anything-drama',
    version='1.0.0',
    packages=['cli_anything.drama'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-drama=cli_anything.drama:cli']},
)
