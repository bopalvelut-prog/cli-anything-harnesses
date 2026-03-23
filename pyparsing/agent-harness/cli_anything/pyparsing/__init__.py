import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pyparsing running')
@cli.command()
def start(): click.echo('pyparsing started')
if __name__ == '__main__': cli()
