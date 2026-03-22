from setuptools import setup
setup(
    name='cli-anything-letsencrypt',
    version='1.0.0',
    packages=['cli_anything.letsencrypt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-letsencrypt=cli_anything.letsencrypt:cli']},
)
