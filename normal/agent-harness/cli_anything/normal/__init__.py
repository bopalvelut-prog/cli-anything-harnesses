import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('normal running')
@cli.command()
def start(): click.echo('normal started')
if __name__ == '__main__': cli()
