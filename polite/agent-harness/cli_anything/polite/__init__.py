import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('polite running')
@cli.command()
def start(): click.echo('polite started')
if __name__ == '__main__': cli()
