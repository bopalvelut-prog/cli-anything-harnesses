from setuptools import setup
setup(
    name='cli-anything-approvals',
    version='1.0.0',
    packages=['cli_anything.approvals'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-approvals=cli_anything.approvals:cli']},
)
