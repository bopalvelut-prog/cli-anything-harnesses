import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('true running')
@cli.command()
def start(): click.echo('true started')
if __name__ == '__main__': cli()
