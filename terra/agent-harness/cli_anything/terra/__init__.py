import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def node(): click.echo('Terra node')
@cli.command()
def stake(): click.echo('Terra staking')
if __name__ == '__main__': cli()
