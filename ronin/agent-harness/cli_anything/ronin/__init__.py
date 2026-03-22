import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def transfer(): click.echo('Ronin transfer')
@cli.command()
def stake(): click.echo('Ronin stake')
if __name__ == '__main__': cli()
