import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sequel running')
@cli.command()
def start(): click.echo('sequel started')
if __name__ == '__main__': cli()
