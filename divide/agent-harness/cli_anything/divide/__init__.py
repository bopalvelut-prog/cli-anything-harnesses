import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('divide running')
@cli.command()
def start(): click.echo('divide started')
if __name__ == '__main__': cli()
