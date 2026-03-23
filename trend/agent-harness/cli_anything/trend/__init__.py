import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('trend running')
@cli.command()
def start(): click.echo('trend started')
if __name__ == '__main__': cli()
