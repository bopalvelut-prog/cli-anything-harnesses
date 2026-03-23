from setuptools import setup
setup(
    name='cli-anything-reload',
    version='1.0.0',
    packages=['cli_anything.reload'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-reload=cli_anything.reload:cli']},
)
