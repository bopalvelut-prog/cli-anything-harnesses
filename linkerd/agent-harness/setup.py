from setuptools import setup
setup(
    name='cli-anything-linkerd',
    version='1.0.0',
    packages=['cli_anything.linkerd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-linkerd=cli_anything.linkerd:cli']},
)
