import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('publication running')
@cli.command()
def start(): click.echo('publication started')
if __name__ == '__main__': cli()
