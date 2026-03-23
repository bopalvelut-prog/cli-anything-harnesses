import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('obtain running')
@cli.command()
def start(): click.echo('obtain started')
if __name__ == '__main__': cli()
