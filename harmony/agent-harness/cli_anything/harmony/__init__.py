import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def transfer(): click.echo('Harmony transfer')
@cli.command()
def stake(): click.echo('Harmony stake')
if __name__ == '__main__': cli()
