import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sops running')
@cli.command()
def start(): click.echo('sops started')
if __name__ == '__main__': cli()
