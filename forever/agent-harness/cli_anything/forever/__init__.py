import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('forever running')
@cli.command()
def start(): click.echo('forever started')
if __name__ == '__main__': cli()
