import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('band running')
@cli.command()
def start(): click.echo('band started')
if __name__ == '__main__': cli()
