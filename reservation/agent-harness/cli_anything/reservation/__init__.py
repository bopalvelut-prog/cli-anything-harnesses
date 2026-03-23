import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('reservation running')
@cli.command()
def start(): click.echo('reservation started')
if __name__ == '__main__': cli()
