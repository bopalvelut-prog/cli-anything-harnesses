import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('fan running')
@cli.command()
def start(): click.echo('fan started')
if __name__ == '__main__': cli()
