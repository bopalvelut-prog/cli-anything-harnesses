import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def account(): click.echo('Ontology account')
@cli.command()
def transfer(): click.echo('Ontology transfer')
if __name__ == '__main__': cli()
