import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('heat running')
@cli.command()
def start(): click.echo('heat started')
if __name__ == '__main__': cli()
