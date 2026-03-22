import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def contacts(): click.echo('Zoho contacts')
@cli.command()
def deals(): click.echo('Zoho deals')
if __name__ == '__main__': cli()
