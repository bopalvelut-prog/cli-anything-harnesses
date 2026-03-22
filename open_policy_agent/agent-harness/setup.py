from setuptools import setup
setup(
    name='cli-anything-open_policy_agent',
    version='1.0.0',
    packages=['cli_anything.open_policy_agent'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-open_policy_agent=cli_anything.open_policy_agent:cli']},
)
