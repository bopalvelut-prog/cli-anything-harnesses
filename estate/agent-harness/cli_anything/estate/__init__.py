import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('estate running')
@cli.command()
def start(): click.echo('estate started')
if __name__ == '__main__': cli()
