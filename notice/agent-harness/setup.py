from setuptools import setup
setup(
    name='cli-anything-notice',
    version='1.0.0',
    packages=['cli_anything.notice'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-notice=cli_anything.notice:cli']},
)
