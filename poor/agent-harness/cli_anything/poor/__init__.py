import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('poor running')
@cli.command()
def start(): click.echo('poor started')
if __name__ == '__main__': cli()
