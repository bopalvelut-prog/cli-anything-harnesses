import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('OPNsense running')
@cli.command()
def services(): click.echo('Running services')
if __name__ == '__main__': cli()
