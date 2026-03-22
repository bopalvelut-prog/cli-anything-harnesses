import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def transfer(): click.echo('Celo transfer')
@cli.command()
def vote(): click.echo('Celo vote')
if __name__ == '__main__': cli()
