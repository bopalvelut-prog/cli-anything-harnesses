import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('transformation running')
@cli.command()
def start(): click.echo('transformation started')
if __name__ == '__main__': cli()
