import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def contacts(): click.echo('HubSpot contacts')
@cli.command()
def deals(): click.echo('HubSpot deals')
if __name__ == '__main__': cli()
