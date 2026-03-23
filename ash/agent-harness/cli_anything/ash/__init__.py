import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ash running')
@cli.command()
def start(): click.echo('ash started')
if __name__ == '__main__': cli()
