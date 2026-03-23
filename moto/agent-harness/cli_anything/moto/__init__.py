import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('moto running')
@cli.command()
def start(): click.echo('moto started')
if __name__ == '__main__': cli()
