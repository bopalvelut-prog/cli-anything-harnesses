import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Hetzner status')
@cli.command()
def servers(): click.echo('Hetzner servers')
if __name__ == '__main__': cli()
