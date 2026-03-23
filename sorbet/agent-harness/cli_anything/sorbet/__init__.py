import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sorbet running')
@cli.command()
def start(): click.echo('sorbet started')
if __name__ == '__main__': cli()
