from setuptools import setup
setup(
    name='cli-anything-gcp_translate',
    version='1.0.0',
    packages=['cli_anything.gcp_translate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gcp_translate=cli_anything.gcp_translate:cli']},
)
