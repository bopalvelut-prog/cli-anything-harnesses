import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('selection running')
@cli.command()
def start(): click.echo('selection started')
if __name__ == '__main__': cli()
