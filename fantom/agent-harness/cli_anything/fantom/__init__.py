import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def transfer(): click.echo('Fantom transfer')
@cli.command()
def stake(): click.echo('Fantom stake')
if __name__ == '__main__': cli()
