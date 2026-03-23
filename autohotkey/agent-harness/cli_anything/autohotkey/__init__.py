import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('autohotkey running')
@cli.command()
def start(): click.echo('autohotkey started')
if __name__ == '__main__': cli()
