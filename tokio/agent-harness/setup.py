from setuptools import setup
setup(
    name='cli-anything-tokio',
    version='1.0.0',
    packages=['cli_anything.tokio'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tokio=cli_anything.tokio:cli']},
)
