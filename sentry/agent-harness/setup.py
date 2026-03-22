from setuptools import setup
setup(
    name='cli-anything-sentry',
    version='1.0.0',
    packages=['cli_anything.sentry'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sentry=cli_anything.sentry:cli']},
)
