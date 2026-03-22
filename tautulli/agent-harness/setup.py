from setuptools import setup
setup(
    name='cli-anything-tautulli',
    version='1.0.0',
    packages=['cli_anything.tautulli'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tautulli=cli_anything.tautulli:cli']},
)
