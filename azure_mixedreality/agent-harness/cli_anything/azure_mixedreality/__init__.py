import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('azure_mixedreality running')
@cli.command()
def start(): click.echo('azure_mixedreality started')
if __name__ == '__main__': cli()
