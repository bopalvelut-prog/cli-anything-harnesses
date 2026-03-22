import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def deals(): click.echo('Pipedrive deals')
@cli.command()
def contacts(): click.echo('Pipedrive contacts')
if __name__ == '__main__': cli()
