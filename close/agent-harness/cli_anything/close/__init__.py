import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('close running')
@cli.command()
def start(): click.echo('close started')
if __name__ == '__main__': cli()
