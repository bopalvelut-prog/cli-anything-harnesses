import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('neither running')
@cli.command()
def start(): click.echo('neither started')
if __name__ == '__main__': cli()
