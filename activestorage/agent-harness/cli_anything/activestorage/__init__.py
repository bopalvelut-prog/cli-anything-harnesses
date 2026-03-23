import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('activestorage running')
@cli.command()
def start(): click.echo('activestorage started')
if __name__ == '__main__': cli()
