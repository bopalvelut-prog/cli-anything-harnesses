from setuptools import setup
setup(
    name='cli-anything-alibaba_cloud',
    version='1.0.0',
    packages=['cli_anything.alibaba_cloud'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-alibaba_cloud=cli_anything.alibaba_cloud:cli']},
)
