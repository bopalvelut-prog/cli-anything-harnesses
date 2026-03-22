import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def init(): subprocess.run(['packer', 'init', '.'])
@cli.command()
def build(): subprocess.run(['packer', 'build', '.'])
@cli.command()
def validate(): subprocess.run(['packer', 'validate', '.'])
if __name__ == '__main__': cli()
