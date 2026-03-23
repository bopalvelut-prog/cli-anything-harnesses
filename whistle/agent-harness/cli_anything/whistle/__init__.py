import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('whistle running')
@cli.command()
def start(): click.echo('whistle started')
if __name__ == '__main__': cli()
