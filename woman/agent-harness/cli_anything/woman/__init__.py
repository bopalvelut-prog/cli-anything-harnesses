import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('woman running')
@cli.command()
def start(): click.echo('woman started')
if __name__ == '__main__': cli()
