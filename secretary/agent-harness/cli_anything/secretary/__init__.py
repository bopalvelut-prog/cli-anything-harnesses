import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('secretary running')
@cli.command()
def start(): click.echo('secretary started')
if __name__ == '__main__': cli()
