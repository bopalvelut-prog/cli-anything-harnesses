import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def serve(): subprocess.run(['vue-cli-service', 'serve'])
@cli.command()
def build(): subprocess.run(['vue-cli-service', 'build'])
@cli.command()
def test(): subprocess.run(['vue-cli-service', 'test:unit'])
if __name__ == '__main__': cli()
