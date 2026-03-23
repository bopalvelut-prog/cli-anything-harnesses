import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('type running')
@cli.command()
def start(): click.echo('type started')
if __name__ == '__main__': cli()
