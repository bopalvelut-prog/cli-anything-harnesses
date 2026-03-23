import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('highlights running')
@cli.command()
def start(): click.echo('highlights started')
if __name__ == '__main__': cli()
