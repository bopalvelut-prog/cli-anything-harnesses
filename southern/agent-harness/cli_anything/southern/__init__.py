import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('southern running')
@cli.command()
def start(): click.echo('southern started')
if __name__ == '__main__': cli()
