import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('typeahead running')
@cli.command()
def start(): click.echo('typeahead started')
if __name__ == '__main__': cli()
