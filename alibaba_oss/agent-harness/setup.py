from setuptools import setup
setup(
    name='cli-anything-alibaba_oss',
    version='1.0.0',
    packages=['cli_anything.alibaba_oss'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-alibaba_oss=cli_anything.alibaba_oss:cli']},
)
