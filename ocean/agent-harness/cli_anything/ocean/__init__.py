import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ocean running')
@cli.command()
def start(): click.echo('ocean started')
if __name__ == '__main__': cli()
