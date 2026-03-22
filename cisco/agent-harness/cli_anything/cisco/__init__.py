import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Cisco router running')
@cli.command()
def config(): click.echo('Running configuration')
if __name__ == '__main__': cli()
