import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('voyager running')
@cli.command()
def start(): click.echo('voyager started')
if __name__ == '__main__': cli()
