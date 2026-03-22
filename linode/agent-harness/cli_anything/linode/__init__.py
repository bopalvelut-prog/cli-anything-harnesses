import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def login(): click.echo('Linode login')
@cli.command()
def instances(): subprocess.run(['linode-cli', 'linodes', 'list'])
if __name__ == '__main__': cli()
