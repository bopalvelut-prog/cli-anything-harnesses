from setuptools import setup
setup(
    name='cli-anything-launchdarkly',
    version='1.0.0',
    packages=['cli_anything.launchdarkly'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-launchdarkly=cli_anything.launchdarkly:cli']},
)
