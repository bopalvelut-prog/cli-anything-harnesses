import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('fabric running')
@cli.command()
def start(): click.echo('fabric started')
if __name__ == '__main__': cli()
