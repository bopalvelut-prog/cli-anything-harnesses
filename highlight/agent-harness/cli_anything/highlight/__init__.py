import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('highlight running')
@cli.command()
def start(): click.echo('highlight started')
if __name__ == '__main__': cli()
