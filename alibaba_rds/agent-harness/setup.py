from setuptools import setup
setup(
    name='cli-anything-alibaba_rds',
    version='1.0.0',
    packages=['cli_anything.alibaba_rds'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-alibaba_rds=cli_anything.alibaba_rds:cli']},
)
