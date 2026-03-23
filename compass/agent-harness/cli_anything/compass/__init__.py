import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('compass running')
@cli.command()
def start(): click.echo('compass started')
if __name__ == '__main__': cli()
