import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('university running')
@cli.command()
def start(): click.echo('university started')
if __name__ == '__main__': cli()
