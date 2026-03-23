from setuptools import setup
setup(
    name='cli-anything-karpenter',
    version='1.0.0',
    packages=['cli_anything.karpenter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-karpenter=cli_anything.karpenter:cli']},
)
