from setuptools import setup
setup(
    name='cli-anything-studio',
    version='1.0.0',
    packages=['cli_anything.studio'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-studio=cli_anything.studio:cli']},
)
