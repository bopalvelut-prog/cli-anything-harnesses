import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pihole running')
@cli.command()
def start(): click.echo('pihole started')
if __name__ == '__main__': cli()
