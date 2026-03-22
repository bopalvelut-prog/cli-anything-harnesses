import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def deals(): click.echo('Freshsales deals')
@cli.command()
def contacts(): click.echo('Freshsales contacts')
if __name__ == '__main__': cli()
