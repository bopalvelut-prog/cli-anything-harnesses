import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('fear running')
@cli.command()
def start(): click.echo('fear started')
if __name__ == '__main__': cli()
