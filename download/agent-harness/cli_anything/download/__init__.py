import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('download running')
@cli.command()
def start(): click.echo('download started')
if __name__ == '__main__': cli()
