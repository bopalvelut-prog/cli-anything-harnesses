import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bundle running')
@cli.command()
def start(): click.echo('bundle started')
if __name__ == '__main__': cli()
