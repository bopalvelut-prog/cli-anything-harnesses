from setuptools import setup
setup(
    name='cli-anything-chatwoot',
    version='1.0.0',
    packages=['cli_anything.chatwoot'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chatwoot=cli_anything.chatwoot:cli']},
)
