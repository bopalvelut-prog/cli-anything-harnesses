import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gauge running')
@cli.command()
def start(): click.echo('gauge started')
if __name__ == '__main__': cli()
