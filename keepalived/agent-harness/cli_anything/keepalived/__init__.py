import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('keepalived running')
@cli.command()
def start(): click.echo('keepalived started')
if __name__ == '__main__': cli()
