import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('barn running')
@cli.command()
def start(): click.echo('barn started')
if __name__ == '__main__': cli()
