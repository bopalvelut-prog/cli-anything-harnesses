import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('industry running')
@cli.command()
def start(): click.echo('industry started')
if __name__ == '__main__': cli()
