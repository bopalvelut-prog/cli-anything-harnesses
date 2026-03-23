import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gotty running')
@cli.command()
def start(): click.echo('gotty started')
if __name__ == '__main__': cli()
